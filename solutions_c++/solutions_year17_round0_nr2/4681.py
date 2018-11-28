#include <bits/stdc++.h>
using namespace std;


int main(int, char**) {
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    long long T;
    fin >> T;
    for (long long t = 0; t < T; ++t) {
        string s;
        fin >> s;
        int i = 0;
        for (; i < s.length()-1; ++i)
            if (s[i] > s[i+1])
                break;
        if (i < s.length() - 1 && s[i] > s[i+1]) {
            int k = i;
            while (k >= 0 && s[k] > s[k+1]) {
                s[k] -= 1;
                --k;
            }
            for (int j = k+2; j < s.length(); ++j)
                s[j] = '9'; 
        }
        
        fout << "CASE #" << t+1L << ": ";
        i = 0;
        while (s[i] == '0')
             ++i;
        fout << s.substr(i) << "\n";
    }
    return 0;
}
