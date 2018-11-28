#include <functional>
#include <iostream>
#include <deque>
#include <set>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long


int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        int R,C;
        cin>>R>>C;
        string S[25];
        for (int i=0;i<R;++i) {
            cin>>S[i];
        }

        set<char> used;

        for (int r=0;r<R;++r) {
            for (int c=0;c<C;++c) {
                if (S[r][c] == '?' || used.count(S[r][c]) > 0) continue;
                used.emplace(S[r][c]);
                int lt = c, rt = c;
                while (lt > 0 && S[r][lt-1] == '?') {
                    lt--;
                }
                while (rt+1 < C && S[r][rt+1] == '?') {
                    rt++;
                }
                //printf ("Doing %c, got %d to %d\n", S[r][c], lt, rt);
                int dir = 1;
                int rw = r;
                while (rw < R) {
                    bool good = true;
                    for (int i=lt;i<=rt;++i) {
                        if (!(S[rw][i] == '?' || S[rw][i] == S[r][c])) {
                            good = false;
                            break;
                        }
                    }
                    if (good) {
                        //printf("Good at %d\n", rw);
                        for (int i=lt;i<=rt;++i) {
                            S[rw][i] = S[r][c];
                        }
                    } else break;
                    rw += dir;
                }
                dir = -1;
                rw = r;
                while (rw >= 0) {
                    bool good = true;
                    for (int i=lt;i<=rt;++i) {
                        if (!(S[rw][i] == '?' || S[rw][i] == S[r][c])) {
                            good = false;
                            break;
                        }
                    }
                    if (good) {
                        //printf("Good at %d\n", rw);
                        for (int i=lt;i<=rt;++i) {
                            S[rw][i] = S[r][c];
                        }
                    } else break;
                    rw += dir;
                }
            }
        }


        printf("Case #%d:\n", t);
        for (int i=0;i<R;++i) {
            printf("%s\n", S[i].c_str());
        }
    }
}

