#include <iostream>
#include <string>

using namespace std;

int ctoi(char c) {
    if (c > '9') {
        return 9;
    }

    return c - '0';
}

int main() {
    string line;  // Used for reading all lines from stdin

    getline(cin, line);
    int testCount = stoi(line);

    for (int i = 1; i <= testCount; i++) {
        getline(cin, line);

        int numDigits = line.length();
        int prevDigit = ctoi(line.at(0));
        int inflection = -1;
        for (int i = 1; i < numDigits; i++) {
            int currDigit = ctoi(line.at(i));

            if (currDigit < prevDigit) {
                inflection = i - 1;
                break;
            }

            prevDigit = currDigit;
        }

        while (inflection > 0) {
            int preDigit = ctoi(line.at(inflection - 1));
            int currDigit = ctoi(line.at(inflection));
            if (currDigit - 1 >= preDigit) {
                break;
            }
            inflection--;
        }

        if (inflection != -1)
        {
            char replaceChar = line.at(inflection) - 1;
            line.replace(inflection, 1, &replaceChar);

            line = line.substr(0, inflection + 1);

            int numberOfNines = numDigits - inflection - 1;
            for (int i = 0; i < numberOfNines; i++) {
                line.append("9");
            }   

            // Remove leading 0
            if (line.at(0) == '0') {
                line.erase(0, 1);
            }
        }

        cout << "Case #" << i << ": " << line << endl;
    }

    return 0;
}
