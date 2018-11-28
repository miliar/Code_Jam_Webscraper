#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void tidying(string &s, int ind) {
    if (ind == 0 && s[ind] == '1') {
        s.erase(s.begin());
        ind--;
    }
    else
        s[ind]--;
    for (int i = ind + 1; s[i] != '\0'; i++)
        s[i] = '9';
}

void tidy(string &s) {
    for (int i = 1; s[i] != '\0'; i++) {
        if (s[i-1] > s[i]) {
            tidying(s, i-1);
            i = 1;
        }
    }
    if (s[1] != '\0' && s[0] > s[1]) {
        tidying(s, 0);
    }
}

int main() {
    ifstream in;
    ofstream out;
    in.open("B-large.in");
    out.open("output.txt");
    int T;
    in >> T;
    int i;

    string s;
    for (i = 0; i < T; i++) {
        in >> s;
        tidy(s);
        out << "Case #" << i + 1 << ": " << s << endl;
    }
    return 0;
}
