print('Odpovidej "ano" nebo "ne".')
stastna = input('Jsi stastna?')
bohata = input('Jsi bohata?')

if stastna == 'ano':
    if bohata == 'ano':
        print('Gratuluji!')
    else:
        print('Zkus min utracet.')
else:
    if bohata == 'ano':
        print('Zkus se vic usmivat!')
    else:
        print('To je mi lito.')