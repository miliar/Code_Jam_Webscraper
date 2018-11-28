#include <bits/stdc++.h>
using namespace std;

int A[25][25];
vector<pair<pair<int, int>, int> > v;

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, tI, R, C, r, l, h, i, j, k;
    char c;
    scanf("%d", &T);
    for (tI = 0; tI < T; tI++) {
        v.clear();
        l = r = 0;
        h = -1;
        scanf("%d %d", &R, &C);
        for (i = 0; i < R; i++) {
            scanf("\n");
            for (j = 0; j < C; j++) {
                scanf("%c", &c);
                if (c != '?') {
                    v.push_back(make_pair(make_pair(i, j), c - 'A'));
                    h = max(h, i);
                }
            }
        }
        sort(v.begin(), v.end());
        for (i = 0; i < v.size(); i++) {
            for (j = l; j < v[i].first.first + 1; j++) for (k = r; k < v[i].first.second + 1; k++) A[j][k] = v[i].second;
            if (i > (int) v.size() - 2) for (j = l; j < R; j++) for (k = r; k < C; k++) A[j][k] = v[i].second;
            else {
                if (v[i].first.first == h) for (j = v[i].first.first + 1; j < R; j++) for (k = r; k < v[i].first.second + 1; k++) A[j][k] = v[i].second;
                r = v[i].first.second + 1;
                if (v[i].first.first < v[i + 1].first.first) {
                    for (j = l; j < v[i].first.first + 1; j++) for (k = v[i].first.second + 1; k < C; k++) A[j][k] = v[i].second;
                    l = v[i].first.first + 1;
                    r = 0;
                }
            }
        }
        printf("Case #%d: \n", tI + 1);
        for (i = 0; i < R; i++) {
            for (j = 0; j < C; j++) printf("%c", A[i][j] + 'A');
            printf("\n");
        }
    }
    return 0;
}
