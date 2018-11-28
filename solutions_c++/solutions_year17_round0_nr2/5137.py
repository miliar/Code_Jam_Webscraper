#include<bits/stdc++.h>
#define INF 0x7fffffff
#define INFLL 1e17
#define PI 2*acos(0.0)
#define show(x) cout<< #x <<" is "<< x <<"\n"
using namespace std;

#define FS first
#define SC second
#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<PII> VPII;

unsigned long long limit, res;


void dfs(unsigned long long val, long long last){
    if (val > limit) {
        return;
    }
    res = max(res, val);

    for (int i = last ; i <= 9; i++) {
        dfs(val * 10 + i, i);
    }
}



int main() {
    #ifndef ONLINE_JUDGE
        freopen("B-large.in", "rt", stdin);
        freopen("outputB.txt", "wt", stdout);
    #endif

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int cas = 0; cas < T; cas++) {
        cin >> limit;
        res = 0;

        for (int i = 1; i <= 9; i++) {
            dfs(i, i);
        }

        cout << "Case #" << cas + 1 << ": " << res << "\n";
    }

return 0;
}
