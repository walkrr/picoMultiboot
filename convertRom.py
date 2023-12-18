def gba_to_c_header(gba_file_path, header_file_path, array_name):
    with open(gba_file_path, 'rb') as file:
        binary_data = file.read()
    hex_data = ', '.join('0x{:02x}'.format(byte) for byte in binary_data)
    with open(header_file_path, 'w') as header_file:
        header_file.write(f"unsigned char {array_name}[] = {{\n    {hex_data}\n}};\n")


gba_to_c_header('rom.gba', 'output.hpp', 'gba_array')
