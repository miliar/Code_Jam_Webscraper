#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
void print(int testNum, const string& ans = "IMPOSSIBLE") {
    cout << "Case #" << testNum << ": " << ans << endl;
}

int main(void) {
    freopen("/Users/glebone/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/glebone/ClionProjects/bsuir/result.out", "w", stdout);
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        int n;
        cin >> n;
        int R, O, Y, G, B, V;
        cin >> R >> O >> Y >> G >> B >> V;

        int sR = R, sO = O, sY = Y, sG = G, sB = B, sV = V;

        int cnt = (R > 0) + (O > 0) + (Y > 0) + (G > 0) + (B > 0) + (V > 0);
        if (cnt == 2 && Y != 0 && V != 0) {
            if (Y != V) {
                print(test);
            } else {
                string ans;
                for (int i = 1; i <= Y; i++) {
                    ans += "YV";
                }
                print(test, ans);
            }
            continue;
        }

        if (cnt == 2 && G != 0 && R != 0) {
            if (R != G) {
                print(test);
            } else {
                string ans;
                for (int i = 1; i <= R; i++) {
                    ans += "RG";
                }
                print(test, ans);
            }
            continue;
        }

        if (cnt == 2 && O != 0 && B != 0) {
            if (O != B) {
                print(test);
            } else {
                string ans;
                for (int i = 1; i <= O; i++) {
                    ans += "OB";
                }
                print(test, ans);
            }
            continue;
        }

        if ((O && O + 1 > B) || (G && G + 1 > R) || (V && V + 1 > Y)) {
            print(test);
            continue;
        }
        B -= O;
        R -= G;
        Y -= V;


        bool was = true;
        vector<string> ans;
        ans.resize((unsigned long) max(R, 1));

        for (int i = 0; i < max(R, 1); i++) {
            if (Y + B == 0) {
                was = false;
                break;
            }
            if (Y > B) {
                ans[i].push_back('Y');
                Y--;
            } else {
                ans[i].push_back('B');
                B--;
            }
        }

        if (!was) {
            print(test);
            continue;
        }

        for (int i = 0; i < max(R, 1); i++) {
            if (Y + B == 0) {
                break;
            }
            while (true) {
                if (ans[i].back() == 'Y' && B) {
                    ans[i].push_back('B');
                    B--;
                    continue;
                }
                if (ans[i].back() == 'B' && Y) {
                    ans[i].push_back('Y');
                    Y--;
                    continue;
                }
                break;
            }
        }

        if (Y || B) {
            print(test, "IMPOSSIBLE");
            continue;
        }

        string glAns = "";
        for (int i = 0; i < max(1, R); i++) {
            glAns += ans[i];
            if (R) {
                glAns.push_back('R');
            }
        }
        if (glAns[0] == glAns.back()) {
            print(test, "IMPOSSIBLE");
            continue;
        } else {

            string glGl = "";
            for (int i = 0; i < glAns.size(); i++) {
                if (V && glAns[i] == 'Y') {
                    glGl.push_back('Y');
                    while (V) {
                        glGl += "VY";
                        V--;
                    }
                    continue;
                }
                if (G && glAns[i] == 'R') {
                    glGl.push_back('R');
                    while (G) {
                        glGl += "GR";
                        G--;
                    }
                    continue;
                }

                if (O && glAns[i] == 'B') {
                    glGl.push_back('B');
                    while (O) {
                        glGl += "OB";
                        O--;
                    }
                    continue;
                }
                glGl += glAns[i];
            }

            print(test, glGl);
        }
    }
}