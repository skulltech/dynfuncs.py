from argparse import ArgumentParser

from elftools.elf.elffile import ELFFile


def dynamic_functions(binary):
    functions = []
    with open(binary, 'rb') as f:
        elf = ELFFile(f)
        dynsym = elf.get_section_by_name('.dynsym')
        for i in range(dynsym.num_symbols()):
            sym = dynsym.get_symbol(i)
            if sym.entry.st_info.bind == 'STB_GLOBAL' and sym.entry.st_info.type == 'STT_FUNC':
                functions.append(sym.name)
    return functions


def main():
    parser = ArgumentParser(description='display globally bound function symbols defined in an elf binary')
    parser.add_argument('binary', help='elf binary to scan')
    args = parser.parse_args()
    functions = dynamic_functions(args.binary)

    if not functions:
        print(f"Symbol table '.dynsym' does not contain any global functions.")
    if functions:
        print(f"Symbol table '.dynsym' contains {len(functions)} global functions:")
        print('   Num: Name')
        for i, func in enumerate(functions):
            print('%6d: %s' % (i, func))


if __name__ == '__main__':
    main()
