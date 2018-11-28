#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int test(long value);
string getNumber(string number, int pos);
string adjustNumber(string number, int pos);
string subtract(string number, int pos);

int main(int argc, char* argv[]) {
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open(argv[1]);
    outputFile.open(argv[2]);

    int t, i;
    string number;

    string::size_type sz;

    inputFile >> t;

    for (i = 0; i < t; i++) {
        inputFile >> number;
        outputFile << "Case #" << (i+1) << ": " << stol(getNumber(number, (number.length() - 1)), &sz) << endl;
    }

    return 0;
}

string getNumber(string number, int pos) {
    int i;

    for (i = number.length() - 1; i > 0; i--) {
        if (number.at(i) < number.at((i - 1))) {
            number = adjustNumber(number, i);
        }
    }

    return number;
}

string adjustNumber(string number, int pos) {
    int i;

    number = subtract(number, (pos - 1));

    for (i = pos; i < number.length(); i++) {
        number.replace(i, 1, 1, '9');
    }

    return number;
}

string subtract(string number, int pos) {
    char prev = number.at(pos);
    if (pos == 0) {
        number.replace(pos, 1, 1, prev - 1);
        return number;
    }
    if (prev == '0') {
        number.replace(pos, 1, 1, '9');
        return subtract(number, (pos - 1));
    }
    number.replace(pos, 1, 1, prev - 1);
    return number;
}

int test(long value) {
    while (value > 0) {
        cout << value << endl;
        if (value % 10 < ((value/10) % 10)) {
            return -1;
        }
        value = value / 10;
    }

    return 0;
}
