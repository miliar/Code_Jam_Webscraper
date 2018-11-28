#include <iostream>
#include <fstream>

using namespace std;

char flip(char c) {
    if(c == '-') return '+';
    else return '-';
}

int main()
{
    int T;
    ifstream infile;
    ofstream outfile;
    string s;
    int k;

    infile.open("data.in");
    outfile.open("data.out");

    infile >> T;
    for(int i = 0; i < T; i++) {
        infile >> s;
        infile >> k;
        int len = s.length();
        int cnt = 0;

        for(int j = 0; j <= len - k; j++) {
            if(s[j] == '-') {
                cnt += 1;
                for(int jj = 0; jj < k; jj++) {
                    s[j + jj] = flip(s[j + jj]);
                }
            }
        }

        for(int j = 0; j < len; j++) {
            if(s[j] == '-') cnt = -1;
        }

        if(cnt == -1) outfile <<"Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
        else outfile <<"Case #" << i + 1 << ": " << cnt << endl;
    }
    return 0;
}
