
#include <bits/stdc++.h>
using namespace std;

string firstNeg(const string& s) {
    int i = 0;
    for (; i<s.size(); i++) {
        if (s[i] == '-') break;
    }
    return s.substr(i);
}   

void flip(string& s, int k) {
    for (int j=0; j<k; j++) {
        if (s[j] == '+') s[j] = '-';
        else s[j] = '+';
    }
}

int minFlips(string s, int k) {
    int flip_count = 0;
    s = firstNeg(s);
    while (s != "") {
        if (k > s.size())
            return -1;
        //cout << "before flip " << s << endl;
        flip(s, k);
        //cout << "flipped " << s << endl;
        flip_count++;
        s = firstNeg(s);
    }
    return flip_count;
}

int main(int argc, char* argv[]) {
    ifstream infile(argv[1]);
    ofstream outfile(argv[2]);
    int T, K;
    string S;
    infile >> T;
    for (int i=1; i<=T; i++) {
        infile >> S >> K;
        int ans = minFlips(S, K);
        outfile << "Case #" << i << ": "; 
        if (ans == -1) 
            outfile << "IMPOSSIBLE" << endl; 
        else 
            outfile << ans << endl;
    }
    outfile.close();
    infile.close();
}
