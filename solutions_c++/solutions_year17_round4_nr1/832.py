
#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int N = 111;

int p, cnt[4];

int8_t memo[4][N][N][N][N];
int go(int r, int cnt[]) {
    int s = cnt[0] + cnt[1] + cnt[2] + cnt[3];
    if (s == 0) return 0;

    auto &res = memo[r][cnt[0]][cnt[1]][cnt[2]][cnt[3]];
    if (res != -1) return res;

    res = r == 0;
    int add = 0;
    forn(i,4) if (cnt[i]) {
        cnt[i]--;
        add = max(add, go((r+i)%p, cnt));
        cnt[i]++;
    }
    res += add;
    return res;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ": ";
        memset(cnt,0,sizeof cnt);

        int n; cin >> n >> p;
        while (n--) {
            int x; cin >> x;
            cnt[x%p]++;
        }

        forn(r,p) forn(a,cnt[0]+2) forn(b,cnt[1]+2) forn(c,cnt[2]+2) forn(d,cnt[3]+2)
            memo[r][a][b][c][d] = -1;


//memset(memo,-1,sizeof memo);
        cout << go(0,cnt) << endl;
    }

    return 0;
}
