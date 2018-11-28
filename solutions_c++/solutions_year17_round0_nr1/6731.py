/*
    royalharsh95
   Harsh Vardhan

*/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

#define MAX 1000000001
#define gi(n) scanf("%d", &n)
#define gl(n) scanf("%lld", &n)
#define pi(n) printf("%d\n", n)
#define pl(n) printf("%lld\n", n)
#define all(c) c.begin(), c.end()
#define MOD 1000000007
#define M_PI 3.14159265358979323846
#define mp make_pair
#define F first
#define S second
#define INF 0x3f3f3f3f
#define INT_MAX 2147483647
#define pb push_back
#define read freopen("in.txt", "r", stdin)
#define write freopen("out.txt", "w", stdout)
#define itr(i, c) \
  for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return (n >> b) & 1; }
inline void set_bit(int& n, int b) { n |= two(b); }
inline void unset_bit(int& n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) {
  int res = 0;
  while (n && ++res) n -= n & (-n);
  return res;
}

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> lli;
typedef pair<int, pii> i3;

ll pwr(ll base, ll p, ll mod = MOD){
    ll ans = 1;
    while(p){
        if(p & 1)   ans = (ans * base) % mod;
        base = (base * base) % mod;
        p /= 2;
    }
    return ans;
}

ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}


ll lcm(ll a, ll b){
    return (a*b) / gcd(a, b);
}

int main()
{
    read;
    write;
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    for(int tt = 1; tt <= t; tt++) {
        int k; string s;
        cin >> s >> k;
        cout << "Case #" << tt << ": ";
        int len = s.size();
        int cnt = 0;
        for(int i = len - 1; i >= k - 1; i--) {
            if(s[i] == '-') {
                int flip = k;
                for(int j = i; ;j--) {
                    if(flip == 0) break;
                    else {
                        if(s[j] == '-') {
                            s[j] = '+';
                        } else if(s[j] == '+') {
                            s[j] = '-';
                        }
                    }
                    flip--;
                }
                cnt++;
            }
        }
        int flag = 0;
        for(int i = 0; i < len; i++) {
            if(s[i] == '-') {
                flag = 1;
                break;
            }
        }
        if(flag == 0) {
            cout << cnt << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}

