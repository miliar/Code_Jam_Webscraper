#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool valid;

void flipping(string &s, int i) {
    if (s[i] == '\0') {
        valid = false;
        return;
    }
    s[i] == '-' ? s[i] = '+' : s[i] = '-';
}

int flip(string &s, int K) {
    int flipped = 0;
    for (int i = 0; s[i+K-1] != '\0'; i++) {
        if (s[i] == '-') {
            for (int j = 0; j < K; j++) {
                flipping(s, i+j);
            }
            flipped++;
        }
    }
    return flipped;
}


int main() {
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    int T;
    in >> T;
    vector<string> s;
    int K[T];
    int i = 0;
    while(i < T) {
        string s1;
        in >> s1;
        s.push_back(s1);
        in >> K[i++];
    }

    int f;

    for (i = 0; i < T; i++) {
        valid = true;

        f = flip(s[i], K[i]);

        for (int j = 0; s[i][j] != '\0'; j++) {
            if (s[i][j] == '-') {
                valid = false;
            }
        }

        out << "Case #" << i + 1 << ": ";
        if (valid)
            out << f;
        else
            out << "IMPOSSIBLE";
        out << '\n';
    }
/*
    i = 0;

    for (vector<string>::iterator it = s.begin(); it != s.end(); it++)
        cout << *it << " K: " << K[i++] << endl;
*/
    return 0;
}
