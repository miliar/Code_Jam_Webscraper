//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

// red + yellow => orange
// yellow + blue => green
// red + blue => violet

bool ok(char a, char b) {
    if (a == b) return false;
    switch (a) {
        case 'R':
            return b != 'O' && b != 'V';
        case 'Y':
            return b != 'O' && b != 'G';
        case 'B':
            return b != 'G' && b != 'V';
        case 'O':
            return b != 'R' && b != 'Y';
        case 'G':
            return b != 'Y' && b != 'B';
        case 'V':
            return b != 'R' && b != 'B';
    }
    return true;
}

bool ok(string s) {
    s += s[0];
    for (int i = 0; i+1 < s.size(); ++i)
    if (!ok(s[i], s[i+1])) {
        return false;
    }
    return true;
}

int main() {
    srand(31415);
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        cout << "Case #" << t << ": ";
    
        bool found = 0;
        if (n <= 10) {
            string s = "";
            while (r --> 0) s += "R";
            while (o --> 0) s += "O";
            while (y --> 0) s += "Y";
            while (g --> 0) s += "G";
            while (b --> 0) s += "B";
            while (v --> 0) s += "V";
            sort(s.begin(), s.end());
            do {
                if (ok(s)) {
                    cout << s << "\n";
                    found = 1;
                    break;
                }
            } while (next_permutation(s.begin(), s.end()));
            if (!found) {
                cout << "IMPOSSIBLE\n";
                continue;
            }
        }
       
        if (!found) {
            string s = "";
            int rr = r, oo = o, yy = y, gg = g, bb = b, vv = v;
            while (s.length() < n) {
                if (rr > 0) {s += "R"; rr--;}
                if (gg > 0) {s += "G"; gg--;}
                if (yy > 0) {s += "Y"; yy--;}
                if (vv > 0) {s += "V"; vv--;}
                if (bb > 0) {s += "B"; bb--;}
                if (oo > 0) {s += "O"; oo--;}
            }
            if (ok(s)) {
                cout << s << "\n";
                found = 1;
                continue;
            }
        }
        for (int bb = 0; bb <= o && !found; ++bb) { // ================
            if (o > 0 && bb == 0) continue;
            
            int bob = bb - 1;
            int co = o - bb + 1;
            if (2 * bob + co + 1 > b && o > 0) continue;
            int totB = bb + (b - 2 * bob - co - 1);
            if (o == 0) totB = b;
            
            for (int rr = 0; rr <= g && !found; ++rr) { // ================
                if (g > 0 && rr == 0) continue;
                
                int rgr = rr - 1;
                int cg = g - rr + 1;
                
                if (2 * rgr + cg + 1 > r && g > 0) continue;
                int totR = rr + (r - 2 * rgr - cg - 1);
                if (g == 0) totR = r;
                
                for (int yy = 0; yy <= v && !found; ++yy) { // ================
                    if (v > 0 && yy == 0) continue;

                    int yvy = yy - 1;
                    int cv = v - yy + 1;
                    if (2 * yvy + cv + 1 > v && v > 0) continue;
                    int totY = yy + (y - 2 * yvy - cv - 1);
                    if (v == 0) totY = y;
                    
                    int arr[] = {totY, totR, totB};
                    sort(arr, arr + 3);
                    if (arr[0] + arr[1] < arr[2] && arr[2] != 1) continue;
                    
                    vector<string> v1, v2, v3;
                    if (o == 0) {
                        for (int i = 0; i < totB; ++i)
                            v1.push_back("b");
                    } else {
                        for (int i = 0; i < bob; ++i)
                            v1.push_back("bob");
                        string tmp = "";
                        for (int i = 0; i < co; ++i)
                            tmp += "bo";
                        tmp += "b";
                        v1.push_back(tmp);
                        while (v1.size() < totB) {
                            v1.push_back("b");
                        }
                    }
                    
                    if (g == 0) {
                        for (int i = 0; i < totR; ++i)
                            v2.push_back("r");
                    } else {
                        for (int i = 0; i < rgr; ++i)
                            v2.push_back("rgr");
                        string tmp = "";
                        for (int i = 0; i < cg; ++i)
                            tmp += "rg";
                        tmp += "r";
                        v2.push_back(tmp);
                        while (v2.size() < totR) {
                            v2.push_back("r");
                        }
                    }
                    
                    if (v == 0) {
                        for (int i = 0; i < totY; ++i)
                            v3.push_back("y");
                    } else {
                        for (int i = 0; i < yvy; ++i)
                            v3.push_back("yvy");
                        string tmp = "";
                        for (int i = 0; i < cv; ++i)
                            tmp += "yv";
                        tmp += "y";
                        v3.push_back(tmp);
                        while (v3.size() < totY) {
                            v3.push_back("y");
                        }
                    }
                    
                    if (v1.size() > v2.size()) swap(v1, v2);
                    if (v2.size() > v3.size()) swap(v2, v3);
                    if (v1.size() > v2.size()) swap(v1, v2);
                    
                    assert(v1.size() == arr[0]);
                    assert(v2.size() == arr[1]);
                    assert(v3.size() == arr[2]);
                    
                    
                    string res = "";
                    for (int i3 = 0; i3 < v3.size(); ++i3) {
                        res += v3[i3];
                        int left = (int) v3.size() - i3 - 1;
                        if (v1.size() > 0) {
                            res += v1.back(); v1.pop_back();
                            if (v1.size() + v2.size() > left && v2.size() > 0) {
                                res += v2.back(); v2.pop_back();
                            }
                        } else if (v2.size() > 0) {
                            res += v2.back(); v2.pop_back();
                        }
                    }
                    found = 1;
                    assert(res.size() == n);
                    for (int i = 0; i < n; ++i)
                        res[i] = toupper(res[i]);
                    cout << res << "\n";
                }
            }
        }
        
        if (!found) {
            cout << "IMPOSSIBLE\n";
        }
    }
    return 0;
}
