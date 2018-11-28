#include <bits/stdc++.h>
using namespace std;

string solve(vector<bool>& d, int k) {
    int c = 0;
    for (int i = 0; i <= d.size() - k; ++i) {
        if (d[i] == false) {
            for (int j = 0; j < k; ++j) {
                //d[i + j] = (d[i + j] | 1) ^ (d[i + j] & 1);
                if (d[i + j])
                    d[i + j] = false;
                else
                    d[i + j] = true;
            }
            ++c;
        }
    }

    for (int i = 0; i < d.size(); ++i) { 
        if (d[i] == false)
            return "IMPOSSIBLE";  
    }
    return to_string(c);
}

int main(int, char**) {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int T;
    fin >> T;
    for (int t = 0; t < T; ++t) {
        string s;
        fin >> s;
        int K;
        fin >> K;
        vector<bool> d(s.length(), false);
        for (int i = 0; i < s.length(); ++i)
            if (s[i] == '+')
                d[i] = true;

        fout << "CASE #" << t+1 << ": " <<  solve(d, K) << "\n";
    }
    return 0;
}
