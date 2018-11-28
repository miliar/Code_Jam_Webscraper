
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
#define cc5(a,b,c,d, e)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<#e<<": "<<e<<endl;
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

int main() {

    freopen("cin.txt", "r", stdin);
    freopen("cout2.txt", "w", stdout);

//    ios_base::sync_with_stdio(0); 
	int t;
	cin >> t;
	rep(tt, 1, t)
	{
		ll n, k;
		cin >> n >> k;
		printf("Case #%d: ", tt);
		pair < ll, ll > even, odd;
		if(n % 2 == 0)
		{
			even.first = n;
			even.second = 1;
		}
		else
		{
			odd.first = n;
			odd.second = 1;
		}
//			cc4(even.first, even.second, odd.first, odd.second);
		pair < ll, ll > levels[(ll)log2(n) + 1][2];
		levels[0][0] = even;
		levels[0][1] = odd;
		for(ll i = 1; i < log2(n); i++)
		{
			pair < ll, ll > prevEven = even, prevOdd = odd;
			ll a = 0, b = 0, c = 0, d = 0;
			if(prevEven.first != 0)
			{
				b = ((prevEven.first / 2) % 2 == 0 ? (prevEven.first / 2) : (prevEven.first / 2 - 1));
				a = b;
				
				if((prevEven.first / 2) % 2 == 0) a = max(0LL, a - 1);
				else a++;
			}
			d = prevOdd.first / 2;
			c = d;
			
			bool flag = (c != 0 and c % 2 == 0);
			
//			cc4(a, b, c, d);
			
			even.first = (b != 0 ? b : (c % 2 == 0 ? c : 0));
			even.second = prevEven.second;
			odd.first = (a != 0 ? a : (c % 2 == 1 ? c : 0));
			odd.second = prevEven.second;
			if(flag == false)
			{
				odd.second += 2 * prevOdd.second;	
			}	
			else
			{
				even.second += 2 * prevOdd.second;
			}
//			cc4(even.first, even.second, odd.first, odd.second);
			levels[i][0] = even;
			levels[i][1] = odd;
		}
		even = levels[(ll)log2(k)][0];
		odd = levels[(ll)log2(k)][1];
		ll pos = k - pow(2, (ll)log2(k)) + 1;
//		cc5(pos, even.first, even.second, odd.first, odd.second);
		ll ev = even.first;
		ll od = odd.first;
		if(ev > od)
		{
			if(even.second >= pos)
			{
				cout << even.first / 2 << " " << max(0LL, even.first / 2 - 1) << "\n";
			}
			else
			{
				cout << odd.first / 2 << " " << odd.first / 2 << "\n";
			}
		}
		else
		{
			if(odd.second >= pos)
			{
				cout << odd.first / 2 << " " << odd.first / 2 << "\n";
			}
			else
			{
				cout << even.first / 2 << " " << max(0LL, even.first / 2 - 1) << "\n";
			}
		}
	}
}
