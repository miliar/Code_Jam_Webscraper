#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

char res[1000000];
char st[4] = "RYB";
int c[3]; // r, y, b
int d[3]; // g, v, o
int oc[3], od[3];
int cr;

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        int n; scanf("%d", &n);
        scanf("%d %d %d %d %d %d", &c[0], &d[2], &c[1], &d[0], &c[2], &d[1]);

        FO(i,0,3) {
            oc[i] = c[i];
            od[i] = d[i];
        }

        assert(d[0] == 0 && d[1] == 0 && d[2] == 0);
        FO(ITER,0,1000) {
            FO(i,0,3) {
                c[i] = oc[i];
                d[i] = od[i];
            }
            vector<int> v;
            FO(i,0,3) if (c[i]) {
                v.push_back(i);
                int lst = i;
                c[lst]--;
                while (c[0]+c[1]+c[2]) {
                    int j0 = (lst+1)%3;
                    int j1 = (lst+2)%3;
                    if (c[j0] < c[j1]) swap(j0,j1);
                    else if (c[j0] == c[j1]) {
                        if (rand()&1) swap(j0,j1);
                    }

                    lst = j0;
                    v.push_back(lst);
                    c[lst]--;

                    if (c[lst] < 0) goto bad;
                }
                if (lst == i) goto bad;
                else break;
            }
            cr = 0;
            FO(i,0,sz(v)) res[cr++] = st[v[i]];
            res[cr++] = 0;
            printf("Case #%d: %s\n", Z, res);
            goto good;
bad:;
        }
        printf("Case #%d: IMPOSSIBLE\n", Z);
good:;
    }
}

