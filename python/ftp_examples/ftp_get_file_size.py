from ftplib import FTP, all_errors

with FTP('ftp.example.com', 'user', 'pass') as ftp:
    try:
        print(ftp.size('image.png')) # Get size of 'image.png' on server
    except all_errors as error:
        print(f"Error checking image size: {error}")

    try:
        print(ftp.size('test.txt'))
    except all_errors as error:
        print(f"Error checking text file size: {error}")
