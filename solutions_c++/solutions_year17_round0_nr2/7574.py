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
string s,t;
int lst,n;
bool flag;
bool isTidy()
{
	int flag = true;
	for(int i = 0 ; i < s.length()-1 ; i++)
		if(s[i] > s[i+1])
			return false;
	return true;
}
void solve()
{
	if(isTidy())
		return ;
	
	lst = -1;flag = true;n=s.length();
	for(int i = 0 ; i < n-1 ;i++)
	{
		if(s[i] > '1')
			lst = i;
		if(s[i] > s[i+1])
		{
			flag = false;break;
		}
	}
	
	if(flag == true){cout << s << endl;return;}
	else 
	{
		if(lst == -1)
		{
			t = "";
			for(int i = 1 ; i < n ; i++)
				t = t+"9";
		}
		else
		{
			t = "";
			for(int i = 0 ; i < n ; i++)
				if(i < lst)
					t += s[i];
				else if(i == lst)
					t += (char)(s[i]-1);
				else
					t += "9";
		}
		s = t;
		solve();
	}
}
signed main()
{
	int t;
	cin >> t;
	for(int i = 1 ; i <= t; i++)
	{
		//~ s = to_string(i);
		cin >> s;
		PRINT
		solve();
		cout << s << "\n";
	}
	return 0;
}
/*
 *



 
4
132
1000
7
111111111111111110





*/
