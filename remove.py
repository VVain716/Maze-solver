import os
for i in range(5, 22, 2):
    os.system(f'rm -R mazelength{i}')
    if os.path.exists(f'solvedmaze{i}'):
        os.system(f'rm -R solvedmaze{i}')