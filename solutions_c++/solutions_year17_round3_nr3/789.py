//~ mail ID : neernpatel@gmail.com 
//~ Author : DrexDelta 
//~ codechef : drexdelta , hackerRank : drexdelta , codeforces : drexdelta1 
//~ Contact Info : neernpatel@gmail.com , +91-80898 25745

#include <bits/stdc++.h>

using namespace std;

#define F first
#define S second
#define MP make_pair
#define PB push_back
#define UB upper_bound
#define LB lower_bound
#define ER erase
#define EN end()
#define B begin()
#define I insert
#define OPTIMIZE ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define int ll
#define endl "\n"
#define CO cout << 
#define CI cin >> 
#define NL cout << endl;
#define DBG cin >> debug;
#define PI 3.1415926535897932384
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;

const ll maxn=1e3 +5;
const ll MOD = 1e9+7;

bool comparator(int i , int j)
{
    return (i < j);
}

ll power(ll x, ll i)
{
	ll ans = 1;
	while(i > 0)
	{
		if(i&1)
			ans = (ans*x)%MOD;
		i >>=1;
		x = (x*x)%MOD;
	}
	return ans;
}

ll power(ll x, ll i,ll mod)
{
	ll ans = 1;
	while(i > 0)
	{
		if(i&1)
			ans = (ans*x)%mod;
		i >>=1;
		x = (x*x)%mod;
	}
	return ans;
}

ll modInverse(ll x, ll mod)
{
	return power(x , mod-2,mod);
}

bool isPalindrome(string s)
{
	int limit = s.length()/2;
	for(int i =  0 ; i < limit ; i++)
	{
		if(s[i] != s[s.length()-i-1])
			return 0;
	}
	return true;
}

ll gcd(ll x, ll y)
{
	ll t;
	while(y != 0)
	{
		t = x%y;
		x = y;
		y = t;
	}
	return x;
}
bool isPrime(int n)
{
	int root = sqrt(n);
	for(int i = 2 ; i <= root ; i++) if(n%i == 0) return 0;
	return 1;
}	
///////////////////////////////////
// declaration section ////////////
///////////////////////////////////
ld a[maxn] , n , k , addition , sum;
void getInput()
{
	CI n >> k;
	CI sum;
	for(int i = 0 ; i < n ; i++)
		CI a[i];
	sort(a  , a + (int)n);
}
ld mul(int index)
{
	ld ret =1 ;
	for(int i = index ; i < n ;i++)
	{
		ret = ret*a[i];
	}
	return ret;
}

ld ppow(ld x , ld n)
{
	ld ret = 1;
	for(int i = 0 ; i < n ; i++)
	{
		ret = ret*x;
	}
	return ret;
}
void solveHelper()
{
	ld avg;
	
	for(int i = 0 ; i < n ; i++)
	{
		//~ cout << " i " << i << endl;
		sum = sum + a[i];
		avg = sum/((ld)(i+1));
		//~ cout << sum << " " << avg << endl;
		if(i == n-1)
		{
			if(avg >= 1)
			{
				cout<< setprecision(10) << fixed << 1.0000000000 ;
				return;
			}
			else
			{
				cout <<setprecision(10) << fixed << ppow(avg , n); return;
			}
		}
		if(avg < a[i+1])
		{
			//~ cout << " end " << endl;
			cout << setprecision(10) << fixed << (ppow(avg , i+1)) * mul(i+1);
			return;
		}
	}
	
}
void solve()
{
	getInput();
	solveHelper();
}
signed main()
{
	//~ OPTIMIZE
	int testCases;
	CI testCases;
	for(int curTest = 1 ; curTest <= testCases ; curTest++)
		CO "Case #" << curTest << ": " , solve(), NL
	
	return 0;
}

/*
 * 
1 3 3 
1
0 0 .75
* 
*/
