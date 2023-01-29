from pathlib import Path
from art import tprint
import pdfplumber
from gtts import gTTS


def pdf_2_mp3(file_path='tedt.pdf', language='en'):
    """Принимает путь до файла и выбирает язык для озвучки"""
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # проверка есть по данному пути файл и pdf ли он
        print(f'[+] Original file: {Path(file_path).name}')
        # выведем оригинальное имя файла после получения пути до файла
        print('[+] Processing...')
        # обозначим что работа в процессе

        # открывает файл pdf на чтение в двоичном режиме rb флаг
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            # пробегаемся по страницам и извлекаем текст из каждой
        text = ''.join(pages)
        # склеиваем страницы между собой join
        text = text.replace('\n', '')
        # удалим перенос строки чтобы не было длинных пауз при озвучке
        # заменяем replace все переносы станицы на пробел

        #Формирование аудиофайла
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        # получаем имя файла при помощи свойства stem
        my_audio.save(f'{file_name}.mp3')
        # сохраняем аудиофайл под именем
        return f'[+] {file_name}.mp3 saved successfully!\n --- Have a nice day!---'

    else:
        return 'file NOT exist '

def main():
    tprint('PDF>>2>MP3', font='bulbhead')  #выведем логотип программы
    file_path = input('\nEnter a file`s path: ')
    language = input('Choice language: example "ru" or "en" ')
    print(pdf_2_mp3(file_path= file_path, language=language))

if __name__ == '__main__':
    main()
