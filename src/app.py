import os
import requests


def download_files(url, address):
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(address, 'wb') as new_file:
            new_file.write(response.content)
        print("Download finalizado. Salvo em: {}".format(address))
    else:
        response.raise_for_status()


if __name__ == "__main__":
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    OUTPUT_DIR = 'Downloaded_files'

    for i in range(1, 26):
        file_name = os.path.join(OUTPUT_DIR, 'Lecture_Notes_{}.pdf'.format(i))
        download_files(BASE_URL.format(i), file_name)
