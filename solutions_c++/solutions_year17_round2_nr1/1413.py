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

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;

const ll maxn=2e6 +5;
const ll MOD = 1e9+7;
const double error = 0.0000000001;

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

int a[maxn],destination , noOfHorses , x,y;
vector <ii> horses;

bool cmp(ii i , ii j)
{
	if(i.F != j.F) 
	    return (i.F < j.F);
    else
		return i.S < j.S;
}

void getInput()
{
	cin >> destination >> noOfHorses ;
	horses.clear();
	for(int i = 0 ; i < noOfHorses ; i++)
	{
		cin >> x >> y;
		horses.PB({x , y});
	}
	sort(horses.begin() , horses.end() , cmp);
}
double solve()
{
	double maxTime = -1,newTime;
	for(int i = 0 ; i < horses.size() ; i++)
	{
		newTime = ((double)destination - (double)(horses[i].F))/(double)horses[i].S;
		//~ cout << newTime << endl;
		if(newTime > maxTime)
			maxTime = newTime;
	}
	
	return (double(destination)/maxTime)-error;
}
signed main()
{
	//~ OPTIMIZE
	int t;
	cin >> t;
	for(int i =1 ; i <= t ; i++)
	{
		cout << "Case #" << i << ": " ;
		getInput();
		
		cout << fixed << setprecision(10) <<  solve() << endl;
		
	}
	return 0;
}
