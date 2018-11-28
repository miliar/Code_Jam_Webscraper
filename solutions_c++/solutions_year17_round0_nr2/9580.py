
// Bismillahir Rahmanir Rahim
// Mr_Emrul

#include <bits/stdc++.h>
#include <stdio.h>
#include <math.h>
using namespace std;

typedef long long int ll;
typedef pair <int, int> pii;
typedef pair <int, pii> pip;
const ll MX = 1000005;

#define LCM(a,b)        (a / __gcd(a,b) ) *-b
#define gcd(a,b)        __gcd(a,b)
#define all(x)          (x).begin(), (x).end()
#define mem(a, n)       memset(a,n,sizeof(a))
#define for1(i, n)      for(i=1; i<=n; i++)
#define for0(i, n)      for(i=0; i<n; i++)
#define rof0(i, n)      for(i=n-1; i>=0; i--)
#define rof1(i, n)      for(i=n; i>=1; i--)
#define forab(i, a, b)  for(i=a; i<=b; i++)
#define rofab(i, a, b)  for(i=b; i>=a; i--)
#define pb              push_back
#define pbb             pop_back
#define YES             cout << "YES" << endl
#define NO              cout << "NO" << endl
#define sin(s)          getline(cin, s)
#define scf(a)          cin >> a
#define scf2(a, b)      cin >> a >> b
#define scf3(a, b, c)   cin >> a >> b >> c
#define scf4(a,b,c,d)   cin >> a >> b >> c >> d
#define pnf(a)          cout << (a) << endl
#define pnf2(a, b)      cout << (a) << " " << (b) << endl
#define pnf3(a, b, c)   cout << (a) << " " << (b) << " " << (c) << endl
#define pnfa(a)         cout << (a) << " "
#define pf(a)           cout << (a)
#define sp              cout << " "
#define nl              cout << endl
#define sz(n)           n.size()
#define clear(v)        v.clear()
#define bug(n)          cout << ">> " << n << " <<" << endl
#define min3(a, b, c)   min(a, min(b, c))
#define max3(a, b, c)   max(a, max(b, c))
#define in              freopen("in.txt", "r", stdin)
#define out             freopen("out.txt", "w", stdout)
#define fast            ios_base::sync_with_stdio(false);
#define F               first
#define S               second
#define mpp             make_pair

ll ar[MX], br[MX];
//vector <ll> v1, v2, q1, q2;
map <ll, ll> mp, mp2;
//map <string, ll> mp, m;
//map <ll, string> ans;
ll solve(string s)
{
    ll i, sum = 0;
    for1(i, sz(s)-1)
    {
        if(s[i]<s[i-1])
            return 0;
    }
    return 1;
}

int main()
{
    string s, x, ans;
    ll mx, i, l, j, t;
    scf(t);
    ll tc;
    for1(tc, t)
    {
        scf(s);
        l = s.size();
        x = s;
        if(solve(s))
            ans = s;
        else
        {
            rof0(i, l)
            {
                s = x;
                if(s[i]>'0')
                    s[i]--;
                forab(j, i+1, l-1)
                s[j] = '9';
                if(solve(s))
                {
                    ans = s;
                    break;
                }
            }
        }
        ll f=0;
        printf("Case #%lld: ", tc);
        for0(i, sz(ans))
        {
            if(ans[i] != '0')
            {
                f=1;
            }
            if(f)
                pf(ans[i]);
        }
        nl;
    }
}
