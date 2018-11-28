#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int R, O, Y, G, B, V;
int n;

string getString(int R, int Y, int B) {
    string res;
    int maxRYB = max(max(R, Y), B);
    int otherRYB = R + Y + B - maxRYB;
    if (maxRYB > otherRYB) return "HEHE";
    vector<pair<int, char> > vec = {make_pair(R, 'R'),
        make_pair(Y, 'Y'), make_pair(B, 'B')};
    sort(vec.begin(), vec.end());
    reverse(vec.begin(), vec.end());
    char lastCH = 'W';
    for (int k = 0; k < R + Y + B; ++k) {
        int cur = -1, mx = -1;
        for (int i = 0; i < 3; ++i) {
            if (vec[i].second != lastCH) {
                if (vec[i].first > mx) {
                    mx = vec[i].first;
                    cur = i;
                }
            }
        }
        char ch = vec[cur].second;
        vec[cur].first -= 1;
        lastCH = ch;
        res.push_back(ch);
    }
    return res;
}


int main0() {
    int T, ca = 0;
    cin >> T;
    while (T--) {
        bool good_ans = true;
        cin >> n >> R >> O >> Y >> G >> B >> V;
        string ans;
        if (O > R || G > R || V > Y) {
            good_ans = false;
        } else if (O != 0 && O == B) {
            if (Y + G + R + V == 0) {
                for (int i = 0; i < O; ++i) {
                    ans.push_back('B');
                    ans.push_back('O');
                }
            } else good_ans = false;
        } else if (G != 0 && G == R) {
            if (Y + O + B + V == 0) {
                for (int i = 0; i < G; ++i) {
                    ans.push_back('G');
                    ans.push_back('R');
                }
            }
        } else if (V != 0 && V == Y) {
            if (R + O + G + B == 0) {
                for (int i = 0; i < V; ++i) {
                    ans.push_back('V');
                    ans.push_back('Y');
                }
            }
        } else {
            string b1, r1, y1;
            for (int i = 0; i < O; ++i) {
                b1.push_back('B');
                b1.push_back('O');
                B -= 1;
            }
            b1.push_back('B');
            
            for (int i = 0; i < G; ++i) {
                r1.push_back('R');
                r1.push_back('G');
                R -= 1;
            }
            r1.push_back('R');
            
            for (int i = 0; i < V; ++i) {
                y1.push_back('Y');
                y1.push_back('V');
                Y -= 1;
            }
            y1.push_back('Y');
            string ans_tmp = getString(R, Y, B);
            if (ans_tmp == "HEHE") {
                good_ans = false;
            }
            bool fr = true, fb = true, fy = true;
            for (char ch : ans_tmp) {
                if (ch == 'R') {
                    if (fr) {
                        fr = false;
                        ans += r1;
                    } else {
                        ans.push_back('R');
                    }
                }
                if (ch == 'Y') {
                    if (fy) {
                        fy = false;
                        ans += y1;
                    } else {
                        ans.push_back('Y');
                    }
                }
                if (ch == 'B') {
                    if (fb) {
                        fb = false;
                        ans += b1;
                    } else {
                        ans.push_back('B');
                    }
                }
            }
        }
        if (good_ans) {
            printf("Case #%d: %s\n", ++ca, ans.c_str());
        } else {
            printf("Case #%d: IMPOSSIBLE\n", ++ca);
        }
    }
    return 0;
}


void test() {
    while (cin >> R >> Y >> B) {
        cout << getString(R, Y, B) << endl;
    }
}

int main() {
    freopen("bs.txt", "r", stdin);
    freopen("bsout.txt", "w", stdout);
    main0();
}