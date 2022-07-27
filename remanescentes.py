from glpiOps import print_os
from glpiOps import openDriver
from glpiOps import login
import gspread

def main():

    SHEET = "CheckList Inspeção Quadros Elétricos " \
            "BT HU-UFS/EBSERH - 001 (respostas)"

    dvr = openDriver()
    login(dvr)

    gc = gspread.service_account()
    sh = gc.open(SHEET)
    wks = sh.get_worksheet(1)

    num = wks.col_values(6)[1:]
    status = wks.col_values(7)[1:]

    for k in range(len(num)):
        if status[k] != 'Solucionado':
            print_os(num[k], dvr)

    dvr.close()

if __name__ == '__main__':
    main()