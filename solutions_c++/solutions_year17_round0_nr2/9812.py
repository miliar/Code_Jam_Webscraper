#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

string tidy(string number) {

    string result;
    string tmp = number;
    int length = number.length() - 1;
    int check = 0;

    for (int i = length; i >= 0; --i) {
        //cout << "tmp: " << tmp << " " << tmp[i] << endl;

        if (tmp[i] < tmp[i - 1]) {
            check = 1;
        }

        if ( check == 1) {
            if (tmp[length] != '0' ) {
                tmp[length] -= 1;
                i = length + 1;
                check = 0;
            } else {
                for (int j = length; j >= 0; --j) {
                    if (tmp[j] == '0') {
                        tmp[j] = '9';
                    } else if ( tmp[j] == tmp[j-1] ) {
                        tmp[j] = '9';
                    } else {
                        tmp[j] -= 1;
                        check = 0;
                        break;
                    }
                }
            }
        }

    }

    if(tmp[0] == '0') {
        tmp.erase(0,1);
    }

    result = tmp;
    return result;
}

int main(int argc, char *argv[]) {

    if ( argc < 2) {
        cout << "error" << endl;
        return 0;
    }

    ifstream inputFile;
    inputFile.open(argv[1]);
    int size;
    string result, number;

    if ( inputFile.is_open() ) {
        inputFile >> dec >> size;
        for (int i = 0; i < size; ++i) {
            inputFile >> number;
            result = tidy(number);
            cout << "Case #" << i + 1 << ": ";
            cout << result << endl;
        }

    } else {
        cerr << "chyba při otevírání souboru" << endl;
        return 0;
    }

    return 0;
}