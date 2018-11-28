#include <bits/stdc++.h>
using namespace std;

#define INF 0X3F3F3F3F
#define INFL 0x3F3F3F3F3F3F3F3FLL
#define MOD 1000000007
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define sz(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define pow2(x) ((x)*(x))
#define watch(x) cout << #x << " is " << x << endl
#define __ << ' ' << 

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int N = 500050;

int main() {
    int tt, n, p;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%d %d", &n, &p);
        vector<int> cnt(4,0);
        for (int i = 0, x; i < n; i++) {
            scanf("%d", &x);
            cnt[x%p]++;
        }
        printf("Case #%d: ", t);
        int ans = cnt[0];
        if (p == 2) {
            ans += (cnt[1]+1)/2;
            printf("%d\n", ans);
        } else if (p == 3) {
            int aux = min(cnt[1], cnt[2]);
            cnt[1] -= aux;
            cnt[2] -= aux;
            ans += aux + (cnt[1]+2)/3 + (cnt[2]+2)/3;
            printf("%d\n", ans);
        } else {
            int aux = cnt[2]/2;
            ans += aux;
            cnt[2] -= aux;
            aux = min(cnt[1], cnt[3]);
            ans += aux;
            cnt[1] -= aux;
            cnt[3] -= aux;
            if (cnt[2]) {
                if (cnt[1] == cnt[3]) {
                    ans++;
                } else if (cnt[1] > 1) {
                    cnt[1] -= 2;
                    ans++;
                } else if (cnt[3] > 1) {
                    cnt[3] -= 2;
                    ans++;
                }
            }
            ans += (cnt[1]+3)/4 + (cnt[3]+3)/4;
            printf("%d\n", ans);
        }
    }
    return 0;
}