#include <bits/stdc++.h>

#define FO(i,a,b) for (int i=(a);i<(b);i++)
#define sz(v) int(v.size())

using namespace std;

int t;
int n, m;
int y[20005], x[20005];
char c[20005];
int msk[105][105];
int omsk[105][105];

bool cplus(int i, int j) {
    return abs(i-n+1) < abs(j-n+1);
}

bool cminus(int i, int j) {
    return abs(i) < abs(j);
}

bool works(int pl, int mn) {
    int ny = (pl+mn)/2;
    int nx = (pl-mn)/2;
    return 0 <= ny && ny < n && 0 <= nx && nx < n;
}

set<int> pdg, mdg;
set<int> xv, yv;

int main() {
    scanf("%d", &t);
    FO(z,0,t) {
        pdg.clear(); mdg.clear();
        xv.clear(); yv.clear();

        scanf("%d %d", &n, &m);
        FO(i,0,m) {
            scanf(" %c %d %d", c+i, y+i, x+i);
            y[i]--; x[i]--;

            if (c[i] == 'o' || c[i] == '+') {
                pdg.emplace(y[i]+x[i]);
                mdg.emplace(y[i]-x[i]);
            }

            if (c[i] == 'o' || c[i] == 'x') {
                xv.emplace(x[i]);
                yv.emplace(y[i]);
            }
        }

        FO(i,0,n) FO(j,0,n) omsk[i][j] = 0;
        FO(i,0,m) {
            if (c[i] == '+') omsk[y[i]][x[i]] |= 1;
            if (c[i] == 'x') omsk[y[i]][x[i]] |= 2;
            if (c[i] == 'o') omsk[y[i]][x[i]] |= 3;
        }

        vector<int> xs, ys;
        FO(i,0,n) if (!xv.count(i)) xs.push_back(i);
        FO(i,0,n) if (!yv.count(i)) ys.push_back(i);
        FO(i,0,sz(xs)) {
            y[m] = ys[i];
            x[m] = xs[i];
            c[m] = 'x';
            m++;
        }

        vector<int> ps[2], ms[2];
        FO(i,-n+1,n) if (!mdg.count(i)) ms[i&1].push_back(i);
        FO(i,0,2*n-1) if (!pdg.count(i)) ps[i&1].push_back(i);

        FO(t,0,2) {
            sort(ps[t].begin(), ps[t].end(), cplus);
            sort(ms[t].begin(), ms[t].end(), cminus);

            int mns = min(sz(ps[t]),sz(ms[t]));

            FO(i,0,sz(ps[t])) FO(j,0,sz(ms[t])-1) {
                assert(works(ps[t][i], ms[t][j]) >= works(ps[t][i], ms[t][j+1]));
            }

            FO(i,0,sz(ms[t])) FO(j,0,sz(ps[t])-1) {
                assert(works(ps[t][j], ms[t][i]) >= works(ps[t][j+1], ms[t][i]));
            }

            for (int l = mns; l > 0; l--) {
                bool bad = false;
                FO(i,0,l) if (!bad) {
                    if (!works(ps[t][i], ms[t][l-i-1])) {
                        bad = true;
                    }
                }
                if (!bad) {
                    FO(i,0,l) {
                        int ny = (ps[t][i] + ms[t][l-i-1])/2;
                        int nx = (ps[t][i] - ms[t][l-i-1])/2;
                        c[m] = '+';
                        y[m] = ny;
                        x[m] = nx;
                        m++;
                    }
                    break;
                }
            }
        }

        FO(i,0,n) FO(j,0,n) msk[i][j] = 0;
        FO(i,0,m) {
            if (c[i] == '+') msk[y[i]][x[i]] |= 1;
            if (c[i] == 'x') msk[y[i]][x[i]] |= 2;
            if (c[i] == 'o') msk[y[i]][x[i]] |= 3;
        }

        stringstream ss;
        int cnt = 0;
        int score = 0;
        FO(cy,0,n) FO(cx,0,n) {
            if (msk[cy][cx]) {
                if (omsk[cy][cx] != msk[cy][cx]) {
                    ss << "+xo"[msk[cy][cx]-1] << " " << 1+cy << " " << 1+cx << "\n";
                    cnt++;
                }
                int scrs[] = {1,1,2};
                score += scrs[msk[cy][cx]-1];
            }
        }

        printf("Case #%d: %d %d\n%s", z+1, score, cnt, ss.str().c_str());
    }
}

