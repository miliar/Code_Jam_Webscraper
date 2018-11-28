#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;

deque<long long> label, num;
/*
void debug() {
    if(label.size() != num.size()) {
        cout << "size not same" << endl;
        return;
    }
    cout << "hehe" << endl;
    for(int i = 0;i < label.size();i ++) {
        cout << label.at(i) << " " << num.at(i) << endl;
    }
}
*/

#define pi acos(-1.0)

int sa[1010];
int sb[1010];

inline int cal(int a, int b, int c) {
    int tt = a * 1 + b * 2 + c * 3;
    tt %= 4;
    if(tt == 0) return 1;
    else return 0;
}

int main()
{
    //freopen("B-small-attempt4.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum;  scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        memset(sa, 0, sizeof(sa));
        memset(sb, 0, sizeof(sb));
        int n, c, m; scanf("%d%d%d", &n, &c, &m);
        int ta = 0, tb = 0;
        for(int i = 0;i < m;i ++) {
            int p, b; scanf("%d%d", &p, &b);
            if(b == 1) {
                sa[p] ++;
                ta ++;
            } else {
                sb[p] ++;
                tb ++;
            }
        }
        int ans = 0, sw = 0;
        for(int i = 1;i <= n;i ++) {
            if(sa[i] != 0 && sb[i] != 0) {
                if(sa[i] > tb - sb[i]) {
                    if(i == 1) {
                        ans += sa[i];
                        ta -= sa[i];
                        tb = sb[i];
                        sa[i] = 0;
                        for(int j = 1;j <= n;j ++) {
                            if(i != j) {
                                sb[i] = 0;
                            }
                        }
                        break;
                    } else {
                        if(sa[i] >= tb) {
                            ans += sa[i];
                            ta -= sa[i];
                            sw += sb[i];
                            sa[i] = 0;
                            tb = 0;
                            break;
                        }
                        if(sa[i] - (tb - sb[i]) >= sb[i] - (ta - sa[i])) {
                        if(sa[i] - (tb - sb[i]))
                        ans += sa[i];
                        sw += (sa[i] - (tb - sb[i]));
                        for(int j = 1;j <= n;j ++) {
                            if(i != j) {
                                sb[i] = 0;
                            } else {
                                sb[i] -= (sa[i] - (tb - sb[i]));
                            }
                        }
                        tb = sb[i];
                        ta -= sa[i];
                        sa[i] = 0;
                        break;
                        }
                    }
                }
                for(int j = 1;j <= n;j ++) {
                    swap(sa[j], sb[j]);
                }
                swap(ta, tb);
                if(sa[i] > tb - sb[i]) {
                    if(i == 1) {
                        ans += sa[i];
                        ta -= sa[i];
                        tb = sb[i];
                        sa[i] = 0;
                        for(int j = 1;j <= n;j ++) {
                            if(i != j) {
                                sb[i] = 0;
                            }
                        }
                        break;
                    } else {
                        if(sa[i] >= tb) {
                            ans += sa[i];
                            ta -= sa[i];
                            sw += sb[i];
                            sa[i] = 0;
                            tb = 0;
                            break;
                        }
                        ans += sa[i];
                        sw += (sa[i] - (tb - sb[i]));
                        for(int j = 1;j <= n;j ++) {
                            if(i != j) {
                                sb[i] = 0;
                            } else {
                                sb[i] -= (sa[i] - (tb - sb[i]));
                            }
                        }
                        tb = sb[i];
                        ta -= sa[i];
                        sa[i] = 0;
                        break;
                    }
                }
            }
        }
        if((ta != 0) || (tb != 0)) {
            ans += max(ta, tb);
        }
        printf("Case #%d: %d %d\n", cs, ans, sw);
    }
    return 0;
}
