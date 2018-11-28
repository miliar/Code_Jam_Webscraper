#include <iostream>
#include <vector>

#define REP(i, a, b) for(unsigned int i = a; i < b; ++i)

using namespace std;

int main() {
    unsigned int TC; cin >> TC; ++TC;
    while(cin.get() != '\n');
    REP(tc, 1, TC) {
        char ch; vector<char> all;
        while((ch = cin.get())) {
            if (ch == '\n')  {
                // for(auto i : all) cout << (char) (i+'0'); cout << "<-" << endl;
                REP(i, 1, all.size()) {
                    if (all[i] < all[i-1]) {
                        int j = i - 1;
                        while(i < all.size()) all[i++] = 9;
                        all[j] -= 1;
                        // for(auto x : all) cout << (int) x; cout << endl;
                        for(; j > 0; --j) {
                            if (all[j] < all[j-1]) {
                                all[j] = 9; all[j-1]-=1;
                            } else break;
                        }
                        i = all.size();
                    }
                }
                unsigned int i = 0;
                while(all[i] == 0) ++i;
                printf("Case #%d: ", tc);
                for(; i < all.size(); ++i) cout << (int) all[i];
                cout << endl;
                break;
            } else if ( ch - '0' >= 0 && ch - '0' <= 9) {
                all.push_back(ch - '0');
            }
        }
    }
    return 0;
}
