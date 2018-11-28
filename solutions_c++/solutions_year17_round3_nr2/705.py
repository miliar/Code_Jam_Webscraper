#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double dd;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define FOR(i,a,b) for (int (i) = (a); (i) < (b); (i)++)
#define DOW(i,b,a) for (int i = (b); i >= (a); i--)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(),(a).end()
#define fi first
#define se second

template<typename T>
void print_array(T* arr, int num) {
   FOR(i, 0, num) cout << arr[i] << ' ';
   cout << endl;
}

template<typename T> 
void print_vector(vector<T> vec) {
   FOR(i,0,vec.size()) cout << vec[i] << ' ';
   cout << endl;
}

int tc, dp[2][2][730][730],a,b,sa[110],ea[110],sb[110],eb[110], last[2][2][730][730], c = 1;

int bt(int k,int st, int x,int y) {
    if (x > 720 || y > 720) return 100000;
    if (x + y == 1440) return k != st;
    if (last[k][st][x][y] == tc) return dp[k][st][x][y];
    int cur = x + y;
    int ans = 100000;
    int chk = 1, chk2 = 1;
    FOR(i,0,a) {
        if (cur >= sa[i] && cur < ea[i]) {
            chk = 0;
            break;
        }
    }
    FOR(i,0,b) {
        if (cur >= sb[i] && cur < eb[i]) {
            chk2 = 0;
            break;
        }
    }
    if (k == 0) {
        if (chk2) ans = 1 + bt(1,st,x,y+1);
        if (chk) ans = min(ans, bt(0,st,x+1,y));     
    } else {
        if (chk) ans = 1 + bt(0,st,x+1,y);
        if (chk2) ans = min(ans, bt(1,st,x,y+1));     
    }
    last[k][st][x][y] = tc;
    return dp[k][st][x][y] = ans;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("test.txt", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%d", &tc);
    memset(last,-1,sizeof last);
    while(tc--) {
        scanf("%d %d", &a,&b);
        FOR(i,0,a) scanf("%d %d", &sa[i], &ea[i]);
        FOR(i,0,b) scanf("%d %d", &sb[i], &eb[i]);
        printf("Case #%d: %d\n", c++,min(bt(0,0,0,0),bt(1,1,0,0)));
    }
}