#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<int, ii> i3;

int occ[1011];

int main (){
    freopen("a.inp", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        int n, k; cin >> n >> k;

        priority_queue<i3, vector<i3>, less<i3> > q;
        q.push(i3(n + 1, ii(0, n + 1)));
        ii ans;
        while (k > 0){
            int l = q.top ().second.first;
            int r = q.top ().second.second;
            q.pop();
            k--;
            int mid = (l + r) / 2;
            q.push(i3(r-mid,ii(mid, r)));
            q.push(i3(mid-l,ii(l, mid)));
            ans = ii(max (r-mid-1, mid-l-1), min(r-mid-1, mid-l-1));
        }
        cout << "Case #" << t << ": ";
        cout << ans.first << ' ' << ans.second << endl;
    }
    return 0;
}
