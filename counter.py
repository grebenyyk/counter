allowed_chars = set('1234567890,- —')

def parse_range(astr):
    set_astr = set((astr))
    if set_astr.issubset(allowed_chars): 
        if astr.isspace() or (astr.strip()[-1] == ',') or (astr.strip()[-1] == '-') or (astr.strip()[-1] == '—'):
            print('Check your input')
            return False  
        result=set()
        astr = astr.replace('-','–') 
        for part in astr.split(','):
            x=part.split('–')
            result.update(range(int(x[0]),int(x[-1])+1))
        return sorted(result)
    else: 
        print('Check your input')
        return False 
    
num_range = str(input("Please submit the page ranges: "))

if num_range:
    parsed_range = parse_range(num_range)
    if parsed_range:
        print(f'Page numbers: {parsed_range}')
        print(f'Page count: {len(parsed_range)}')
else:
    print('Check your input')