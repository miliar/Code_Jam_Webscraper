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
#define EN end
#define B begin
#define I insert
#define OPTIMIZE ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define int ll
#define endl "\n"
#define PRINT cout << "Case #" << i << ": " ;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;

const ll maxn=2e5 +5;
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
///////////////////////////////////
// declaration section ////////////
///////////////////////////////////
string s;
int pl,mi,ans,i,k;
void flip(int pos)
{
	for(int i = pos; i < pos+k ; i++)
		if(s[i] == '+')s[i]='-',pl--,mi++;
		else s[i]='+',pl++,mi--;
	int debug;
}
int isSolvable()
{
	pl=mi=0;
	for(int j = 0 ; j < s.length() ; j++)
		if(s[j] == '+')pl++;else mi++;
	ans=i=0;
	while(mi != 0)
	{
		if(s[i] == '-')
			if(i+k > s.length())
				break;
			else
				flip(i),ans++;
		else
			i++;
		
	}
	if(mi != 0)return -1;
	return ans;
}
signed main()
{
	//~ OPTIMIZE
	int t;
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
	{
		cin >> s >> k;
		int x = isSolvable();
		PRINT
		if(x==-1)
			cout << "IMPOSSIBLE\n";
		else
			cout << x << "\n";
	}
	return 0;
}
