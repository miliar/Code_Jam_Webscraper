#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int n, p;
vector<int> req;
vector<vector<int> > a;
vector<vector<int> > l;
vector<vector<int> > r;
vector<vector<pair<int, int> > > temp;
vector<int> used;

int main() {
    freopen("Documents/Informatics/GoogleCodeJam/in.txt", "r", stdin);
    freopen("Documents/Informatics/GoogleCodeJam/ratatouille.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int cas = 1; cas <= tc; cas++) {
        int minl = 0;
        int maxr = 10123456;
        req.clear();
        a.clear();
        l.clear();
        r.clear();
        used.clear();
        temp.clear();
        scanf("%d %d", &n, &p);
        req.resize(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &req[i]);
        }
        a.resize(n);
        l.resize(n);
        r.resize(n);
        temp.resize(n);
        used.resize(n);
        for (int i = 0; i < n; i++) {
            used[i] = 0;
            a[i].resize(p);
            l[i].resize(p);
            r[i].resize(p);
            temp[i].resize(p);
            int mini = 10123456;
            int maxi = 0;
            for (int j = 0; j < p; j++) {
                scanf("%d", &a[i][j]);
                l[i][j] = ceil(((double)a[i][j]/1.1f)/req[i] - 0.000001f);
                r[i][j] = floor(((double)a[i][j]/0.9f)/req[i] + 0.000001f);
                if (l[i][j] > r[i][j]) {
                    l[i][j] = 1012345678;
                    r[i][j] = -1;
                }
                else {
                    mini = min(mini, l[i][j]);
                    maxi = max(maxi, r[i][j]);
                }
            }
            minl = max(mini, minl);
            maxr = min(maxi, maxr);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                temp[i][j] = make_pair(l[i][j], r[i][j]);
            }
            sort(temp[i].begin(), temp[i].end());
        }
        /*for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++)
            printf("%d %d %d\n", a[i][j], temp[i][j].first, temp[i][j].second);
        }*/
        int ans = 0;
        int index = 0;
        bool fin = false;
        bool skip = false;
        //printf("%d %d\n", minl, maxr);
        for (int j = minl; j <= maxr; j++) {
            skip = false;
            for (int i = 0; i < n; i++) {
                if (used[i] + index >= p) {
                    fin = true;
                    break;
                }
                //else if (temp[i][used[i]+index].second >= j && j >= temp[i][used[i]+index].first) break;
                while (temp[i][used[i]+index].second < j) {
                    used[i]++;
                    if (used[i] + index >= p) {
                        fin = true;
                        break;
                    }
                }
                if (fin) break;
                if (temp[i][used[i]+index].first > j) {
                    skip = true;
                    break;
                }
            }
            if (fin) break;
            if (skip) continue;
            ans++;
            index++;
            j--;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
