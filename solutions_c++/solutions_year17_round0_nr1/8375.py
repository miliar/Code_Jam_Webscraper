#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

vector<string> possibleFlips;
void GenFlips (int l, string cf) {
    if (cf.length() == l) {
        possibleFlips.push_back(cf);
    } else {
        GenFlips (l,cf+"1");
        GenFlips (l,cf+"0");
    }
}

bool TryPattern (string pat, string str, int k) {
    string p = pat, s = str;
    for (int i = 0; i < p.length(); i++) {
        //Flip on s starting at i
        if (p[i] == '0')
            continue;
        for (int j = i; j < (i+k); j++) {
            s[j] = (s[j] == '+') ? '-' : '+';
        }
    }
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != '+') {
            return false;
        }
    }
    return true;
}

int CountFlips (string pat) {
    int ans = 0;
    for (int i = 0; i < pat.length(); i++) {
        if (pat[i] == '1')
            ans++;
    }
    return ans;
}

int main () {
    ifstream fin ("pancakeSmallIN.txt");
    ofstream fout ("pancakeSmallOUT.txt");
    int T;
    fin >> T;
    for (int t = 0; t < T; t++) {
        string s;
        int k;
        fin >> s >> k;
        possibleFlips.clear();
        int sl = s.length();
        if (k>sl) {
            fout << "Case #" << (t+1) << ": IMPOSSIBLE\n";
            continue;
        }
        GenFlips(s.length()-(k-1),"");
        //Try every flip pattern
        int ans = -1;
        for (int i = 0; i < possibleFlips.size(); i++) {
            if (TryPattern (possibleFlips[i],s,k)) {
                int cf = CountFlips(possibleFlips[i]);
                if (ans == -1 || cf < ans)
                    ans = cf;
            }
        }
        if (ans != -1)
            fout << "Case #" << (t+1) << ": " << ans << "\n";
        else
            fout << "Case #" << (t+1) << ": IMPOSSIBLE\n";
    }
    return 0;
}
