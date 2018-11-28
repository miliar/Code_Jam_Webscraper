#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    //freopen("C-small-1-attempt1.in", "r", stdin);
    //freopen("ans2.txt", "w", stdout);
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int tc; cin >> tc;
    for (int tci = 1; tci <= tc; ++tci) {
        ll n, k; scanf("%lld%lld", &n, &k);
        ll maxi = 0, mini = 0;
        bool arr[n+2]; memset(arr, 0, sizeof arr); arr[0] = arr[n+1] = true;
        int l[n+2], r[n+2];
        memset(l, 0, sizeof l); for (int i = 0; i < n+2; ++i) r[i] = n+1;
        for (int i = 0; i < k; ++i) {
            int ind = 1, mx = 0, mn = 0;
            //for (int j = 0; j < n; ++j) if (!arr[j]) {ind = j; break;}
            for (int j = 0; j < n; ++j) if (!arr[j]) {
                int tmp = min(j-l[j]-1, r[j]-j-1), tmp2 = max(j-l[j]-1, r[j]-j-1);
                //printf("%d %d :: %d %d\n", tmp, tmp2, mx, mn);
                if (tmp > mn) {mn = tmp; mx = tmp2; ind = j;}
                else if (tmp == mn && tmp2 > mx) {mx = tmp2; ind = j;}
            }
            //printf("Heh %d :: %d %d\n", ind, mx, mn);
            arr[ind] = true;
            for (int j = 0; j < n; ++j) {
                if (j < ind && r[j] > ind) r[j] = ind;
                if (j > ind && l[j] < ind) l[j] = ind;
            }
            maxi = mx; mini = mn;
        }
        printf("Case #%d: %lld %lld\n", tci, maxi, mini);
    }
}
