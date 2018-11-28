#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <memory>
#include <utility>

using namespace std;

int main() {
    int t;
    cin >> t;
    for(int ts = 1; ts <= t; ++ts) {
        cout << "Case #" << ts << ":";
        cout << endl;

        int R, C;
        cin >> R >> C;

        vector<string> cake(R);
        vector<vector<bool>> wasthere(R);
        for(int i = 0; i < R; ++i) {
            cin >> cake[i];
            vector<bool> t(C);
            wasthere[i] = t;
        }
        
        int left, right;
        for(int i = 0; i < R; ++i) {
            for(int j = 0; j < C; ++j) {
                string s = cake[i];
                char c = s[j];
                if(!wasthere[i][j] && c != '?') {
                    left = right = j;
                    --left;
                    while(left >= 0 && (s[left] == '?')) {
                        s[left] = c;
                        wasthere[i][left] = true;
                        --left;
                    }
                    ++left;
                    ++right;
                    while(right < C && (s[right] == '?')) {
                        s[right] = c;
                        wasthere[i][right] = true;
                        ++right;
                    }
                    --right;
                    cake[i] = s;

                    int h = i+1;
                    while(h < R) {
                        // cout << left << ' ' << right << endl;
                        string s2 = cake[h];
                        // cout << "testing " << s2 << endl;
                        int temp = left;
                        bool replace = true;
                        while(temp <= right) {
                            if(s2[temp] != '?') { replace = false; break; }
                            ++temp;
                        }
                        if(replace) {
                            // cout << "replacing " << c << endl;
                            temp = left;
                            while(temp <= right) {
                                wasthere[h][temp] = true;
                                s2[temp] = c;
                                ++temp;
                            }
                            cake[h] = s2;
                            ++h;
                        } else {
                            break;
                        }
                    }
                    j = right;
                }
            }
        }

        int h = 0;
        while(h < R && cake[h][0] == '?') {
            ++h;
        }
        string s = cake[h--];
        while(h >= 0) {
            cake[h] = s;
            --h;
        }

        for(int i = 0; i < R; ++i) {
            cout << cake[i] << endl;
        }
    }
}
