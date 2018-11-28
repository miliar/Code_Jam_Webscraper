#include <iostream>
#include <c++/vector>
#include <c++/fstream>

using namespace std;

// 13332
// 12999

struct Solve {
    Solve(string n) {
        for (size_t i = (n.size() - 1); i > 0;) {
            size_t j = i - 1;
            int b = n[i] - '0';
            int a = n[j] - '0';

            if (b < a) {
                while (a == 0) {
                    n[i] = '9';
                    i = j--;
                    a = n[j];
                }
                n[i] = (char) (9 + '0');
                n[j] = (char) (a - 1 + '0');
                for (size_t q = i; q < n.size(); ++q) {
                    n[q] = '9';
                }
            }
            i = j;

        }
        answer = n;
        while (answer[0] == '0') {
            answer = answer.substr(1);
        }
    }
    string answer = "";
};

int main() {

    ofstream ofs;
    ifstream ifs;

    ifs.open("in.txt");
    ofs.open("out.txt", ofstream::out | ofstream::app);


    size_t T; // size of input

    ifs >> T;

    int _case = 1;

    string line;
//    int line;

    while (ifs >> line) {

        Solve solution(line);

        ofs << "Case #" << _case++ << ": " << solution.answer << endl;
    }

    return 0;
}