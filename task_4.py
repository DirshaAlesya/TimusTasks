monsters = int(input(''))

if 1 <= monsters <= 4:
    print('few')
elif 5 <= monsters <= 9:
    print('several')
elif 10 <= monsters <= 19:
    print('pack')
elif 20 <= monsters <= 49:
    print('lots')
elif 50 <= monsters <= 99:
    print('horde')
elif 100 <= monsters <= 249:
    print('throng')
elif 250 <= monsters <= 499:
    print('swarm')
elif 500 <= monsters <= 999:
    print('zounds')
elif 1000 <= monsters <= 2000:
    print('legion')