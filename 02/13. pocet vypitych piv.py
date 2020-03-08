pocet_piv = int(input('Kolik jsi uz dnes vypil piv? '))
if pocet_piv <= 1:
    print('To je slaby!')
elif pocet_piv <=  2:
    print('Hmm, nic moc vykon, pridej!')
elif pocet_piv <= 3:
    print('DOst dobry,kamo!')
elif pocet_piv <= 6:
    print('Tak dame jeste jedno a pujdeme domu, ne?')
elif pocet_piv <= 14:
    print('To se pozna prvoligovy alkoholik!')
elif pocet_piv <= 25:
    print('Preju prijemny pobyt na zachytce')
else:
    print('To uz musis byt mrtvy!')