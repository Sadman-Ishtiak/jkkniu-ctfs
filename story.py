def decode_whitespace_stego(filename):
    with open(filename, 'r') as f:
        data = f.read()

    # Extract only whitespace characters
    whitespace = ''.join(c for c in data if c in [' ', '\t', '\n'])

    # Replace space with '0', tab with '1', split by newline
    binary_lines = whitespace.replace(' ', '0').replace('\t', '1').split('\n')

    hidden_message = ''
    for line in binary_lines:
        if line.strip() == '':
            continue
        try:
            byte = int(line, 2)
            hidden_message += chr(byte)
        except ValueError:
            pass

    return hidden_message

# Usage
flag = decode_whitespace_stego('story.c')
print("Hidden message:", flag)
flag = decode_whitespace_stego('cipher.txt')
print("Hidden message:", flag)
