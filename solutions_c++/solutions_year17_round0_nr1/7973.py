#include <bits/stdc++.h>
using namespace std;
bool allSmile(string s) {
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            return 0;
        }
    }
    return 1;
}
int main() {
    
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T, k;
    in >> T;
    string s;
    for (int i = 0; i < T; ++i) {
        int ans = 0;
        in >> s >> k;
        if (allSmile(s)) {
            out << "Case #" << i + 1 << ": " << ans << endl;
            continue;
        }
        int sz = s.size();
        for (int ii = 0; ii < sz - k; ++ii) {
            if (s[ii] == '-') {
                bool isSmile = 0;
                for (int j = 1; j < k; ++j) {
                    if (s[ii + j] == '+') {
                        ++isSmile;
                        break;
                    }
                }
                if (!isSmile) {
                    for (int j = 0; j < k; ++j) {
                        s[ii + j] = '+';
//                        std::cout << s << '\n';
    
                    }
                    ++ans;
                }
            }
        }
        for (int ii = 0; ii <= sz - k; ++ii) {
            if (s[ii] == '-') {
                for (int j = 0; j < k; ++j) {
                    if (s[ii + j] == '+') {
                        s[ii + j] = '-';
                    } else
                        s[ii + j] = '+';
//                    std::cout << s << '\n';
                    
                }
                ++ans;
            }
        }
        if (allSmile(s)) {
            out << "Case #" << i + 1 << ": " << ans << endl;
        } else
            out << "Case #" << i + 1 << ": IMPOSSIBLE\n";
        
    }
    
}