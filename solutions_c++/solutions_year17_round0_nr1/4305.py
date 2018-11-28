#include <bits/stdc++.h>
#define ll long long int
#define pii pair <int,int>
#define ff first
#define ss second
#define pi acos(-1.0)
#define pb push_back
#define INF (ll)1e17
#define N 100002
#define MOD 1000000007
#define BASE 100003
#define FastRead ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;

template < class T > inline T gcd(T a, T b) {while(b) {a %= b; swap(a, b);} return a;}
template < class T > inline T lcm(T a, T b) {return a/gcd(a, b)*b;}
inline int nxt() {int wow; scanf("%d", &wow); return wow;}
inline ll lxt() {ll wow; scanf("%lld", &wow); return wow;}
inline double dxt() {double wow; scanf("%lf", &wow); return wow;}

/***************** Fighters Launched *******************/

int main()
{
    freopen("A_large.txt", "r", stdin);
    freopen("A_OL.txt", "w", stdout);
    FastRead;
    int t, cse = 0;
    cin >> t;
    while (t--){
        string s;
        int k, flag = 0, cnt = 0;
        cin >> s >> k;
        for (int i=0; i+k-1<s.length(); i++){
            if (s[i] == '-'){
                for (int j=i; j<i+k; j++){
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                cnt++;
            }
        }
        for (int i=0; i<s.length(); i++) if (s[i] == '-') flag = 1;
        cout << "Case #" << ++cse << ": ";
        if (flag) cout << "IMPOSSIBLE";
        else cout << cnt;
        cout << endl;
    }
    return 0;
}
