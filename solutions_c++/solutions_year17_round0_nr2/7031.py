
/**************************************************
**  Author:  Aditya Goel                          *
**  NIT, Kurukshetra                              *  
**  INDIA                                         * 
**************************************************/

#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007  //NA
#define inf 0x3f3f3f3f

#define ll long long int
#define dt ll

#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))

#define rep(i,a,b) for(dt i=a;i<=(dt)(b);i++)

#define tr(container, it) for(vector<dt> :: iterator it= container.begin(); it!=container.end(); it++)
#define trp(container, it) for(vector<pair<dt,dt> > :: iterator it = container.begin(); it!=container.end(); it++)
#define tra(container, it) for(typeof(container.begin()) it = container.begin(); it!=container.end(); it++)

#define scanll(a) scanf("%lld",&a);
#define scani(a) scanf("%d",&a);
#define scand(a) scanf("%lf",&a);

#define cc1(a)cout<<#a<<": "<<a<<endl;
#define cc2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<< endl;
#define cc3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<endl;
#define cc4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<endl;

#define pr pair<dt,dt>  //NA
#define mp(a,b) make_pair(a,b)
#define pb push_back  //NA
#define gc getchar  //NA
#define F first
#define S second

#define vi vector<int>
#define vvl vector<vector<ll>>
#define vii vector<pair<int,int> >
#define pii pair<int,int>
#define plii pair<pair<ll, int>, int>
#define piii pair<pii, int>
#define viii vector<pair<pii, int> >
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define pq priority_queue < dt, vector < dt >, greater < ll > > 
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <tr1/unordered_map>

using namespace std::tr1;

const int mod = 1e9 + 7;
 
ll gcd (ll a, ll b)
{
	return (!b ? a : gcd(b, a % b)); 
}

int ADD(int a, int b, int m = mod) 
{
    int s = a;
    s += b;
    if( s >= m )
      s -= m;
    return s;
}

 

int MUL(int a, int b, int m = mod) 
{
    return (1LL * a * b % m);
}
 
int power(int a, int b, int m = mod) {
    int res = 1;
    while( b ) {
        if( b & 1 ) {
            res = 1LL * res * a % m;
        }
        a = 1LL * a * a % m;
        b /= 2;
    }
    return res;
}
 
int DIV(int a, int b, int m = mod)
{
	return MUL(a, power(b, m - 2));
}
const int SIZE = 1e5+10;
ll fac[SIZE], inv[SIZE];
void build_inverse_modulo()
{
    assert(MOD >= SIZE);
    fac[0] = 1;
    rep(i, 1, SIZE) 
	{
		fac[i] = fac[i-1] * i % MOD;
	}
    inv[SIZE - 1] = power(fac[SIZE - 1], MOD-2, MOD);
    for(int i = SIZE - 2; i >= 0; i--) inv[i] = inv[i + 1] * (i + 1) % MOD;
    for(int i = SIZE - 1;i > 0; i--) inv[i] = inv[i] * fac[i - 1] % MOD;
}
ll ans;

backtracking(ll n, ll m)
{
	ans = max(ans, m);
	for(ll i = 9; i > 0; i--)
	{
		if(m * 10 + i <= n and m % 10 <= i)
		{
			backtracking(n, m * 10 + i);
		}
	}
}

int main() {

    freopen("bin.txt", "r", stdin);
    freopen("bout.txt", "w", stdout);

//    ios_base::sync_with_stdio(0); 
	int t;
	cin >> t;
	rep(tt, 1, t)
	{
		ans = 0;
		ll n;
		cin >> n;
		backtracking(n, 0);
		printf("Case #%d: ", tt);
		cout << ans << "\n";
	}
}
