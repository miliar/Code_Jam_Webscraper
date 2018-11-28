#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int getInt(char c) {
    return c - '0';
}

char getChar(int i) {
    return '0'+i;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("largeout.out");
    int T;
    fin >> T;
    for(int coun = 0; coun < T; coun++) {
        string s;
        fin >> s;
        int prev = getInt(s[0]);
        for(int i = 0; i < s.length(); i++) {
            if(getInt(s[i]) < prev) {
                if(prev > 1) {
                    s[i-1] = getChar(getInt(s[i-1]) - 1);
                } else {
                    s.erase(s.begin());
                    for(int j = 0; j < i; j++) {
                        s[j] = '9';
                    }
                }
                for(int j = i; j < s.length(); j++) {
                        s[j] = '9';
                }
                i = 0;
                prev = getInt(s[0]);
            } else {
                prev = getInt(s[i]);
            }

        }
        fout << "Case #" << coun+1 << ": " << s << '\n';
    }
}
