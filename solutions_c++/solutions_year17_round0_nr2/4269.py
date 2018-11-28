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
//#define FastRead ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;

template < class T > inline T gcd(T a, T b) {while(b) {a %= b; swap(a, b);} return a;}
template < class T > inline T lcm(T a, T b) {return a/gcd(a, b)*b;}
inline int nxt() {int wow; scanf("%d", &wow); return wow;}
inline ll lxt() {ll wow; scanf("%lld", &wow); return wow;}
inline double dxt() {double wow; scanf("%lf", &wow); return wow;}

/***************** Fighters Launched *******************/

string s;

void go (int x, int y){
    if (s[y] < s[x]){
        s[y] = '9';
        s[x]--;
        //cout << "s = " << s << endl;
    }
    else return;
    if (x == 0) return;
    else go (x-1, y-1);
}

int main()
{
    freopen("B_large.txt", "r", stdin);
    freopen("B_OL.txt", "w", stdout);
    int t = nxt(), cse = 0;
    while (t--){
        cin >> s;
        printf("Case #%d: ", ++cse);
        if (s.length() == 1){
            cout << s << endl;
            continue;
        }
        for (int i=1; i<s.length(); i++){
            if (s[i] < s[i-1]){
                go (i-1, i);
                for (int j=i; j<s.length(); j++) s[j] = '9';
                break;
            }
        }
        int start = 0;
        if (s[0] == '0') start = 1;
        for (int i=start; i<s.length(); i++) printf("%c", s[i]);
        cout << endl;
    }
    return 0;
}
