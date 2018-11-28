#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

vector< pair<pii, int> > S;
vector<pii> idx;

int main() {

    // freopen("B-large.in", "r", stdin);
    // freopen("B-large.out", "w", stdout);

    int T, k = 0, ac, aj, i, c, d, t[2], j, m, res;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d%d", &ac, &aj);
        S.clear();
        memset(t, 0, sizeof(t));
        for(i=0;i<ac;i++) {
            scanf("%d%d", &c, &d);
            S.push_back(make_pair(make_pair(c, d), 0));
            t[0] += d - c;
        }
        for(i=0;i<aj;i++) {
            scanf("%d%d", &c, &d);
            S.push_back(make_pair(make_pair(c, d), 1));
            t[1] += d - c;
        }
        sort(S.begin(), S.end());
        idx.clear();
        res = 0;
        for(i=0;i<S.size();i++) {
            j = (i + 1) % S.size();
            if (S[i].second != S[j].second) {
                res++;
                continue;
            }
            c = (1440 + S[j].first.first - S[i].first.second) % 1440;
            idx.push_back(make_pair(c, i));
        }
        sort(idx.begin(), idx.end());
        for(m=0;m<idx.size();m++) {
            c = idx[m].first;
            i = idx[m].second;
            j = (i + 1) % S.size();
            d = min(c, 720-t[S[i].second]);
            if (d < c)
                res += 2;
            t[S[i].second] += d;
            S[i].first.second = (S[i].first.second + d) % 1440;
        }
        printf("%d\n", res);
        /* for(i=0;i<S.size();i++) {
            j = (i + 1) % S.size();
            c = (1440 + S[j].first.first - S[i].first.second) % 1440;
            if (t[S[i].second] < 720) {
                d = min(c, 720-t[S[i].second]);
                t[S[i].second] += d;
                S[i].first.second = (S[i].first.second + d) % 1440;
                c -= d;
            }
            if (t[S[j].second] < 720) {
                d = min(c, 720-t[S[j].second]);
                t[S[j].second] += d;
                S[j].first.first = (1440 + S[j].first.first - d) % 1440;
            }
        } */
    }

    return 0;
}
