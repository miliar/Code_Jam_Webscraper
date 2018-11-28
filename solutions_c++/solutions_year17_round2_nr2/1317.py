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
struct input{
	int counts;
	char c;
};
input inp[10];
int n;
string outputString;

char getColor(int i)
{
	if(i == 0)
		return 'R';
	else if(i == 1)
		return 'O';
	else if(i == 2)
		return 'Y';
	else if(i == 3)
		return 'G';
	else if(i == 4)
		return 'B';
	else if(i == 5)
		return 'V';
}
void getInput()
{
	cin >> n;
	for(int i = 0 ; i < 6 ; i++)
	{
		cin >> inp[i].counts;
		inp[i].c = i;
	}
}
bool isImpossible()
{
	int maxx = -1;
	for(int i = 0 ; i < 6 ; i++)
		if(inp[i].counts > maxx)
			maxx = inp[i].counts;
	if(maxx > (n-maxx))
		return 1;
	return 0;
}
bool cmp(input i , input j)
{
	if(i.counts != j.counts)
	    return (i.counts > j.counts);
	else
		return (i.c > j.c);
}
void solve()
{
	if(isImpossible())
	{
		outputString = "IMPOSSIBLE";
		return;
	}
	int max1 , max2 , i1 , i2;
	outputString = "";
	for(int i = 0 ; i < n ; i++)
		outputString += " ";
	int curColor = 0;
	for(int i = 0 ; i < 6 ; i++)
	{
		if(inp[i].counts > inp[curColor].counts)
			curColor = i;
	}
	for(int i = 0 ; i < n ; i = i+2)
	{
		while(inp[curColor].counts == 0)curColor = (curColor+1)%6;
		if(inp[curColor].counts > 0)
		{
			outputString[i] = getColor(curColor);
			inp[curColor].counts--;
		}
	}
	for(int i = 1 ; i < n ; i = i+2)
	{
		while(inp[curColor].counts == 0)curColor = (curColor+1)%6;
		if(inp[curColor].counts > 0)
		{
			outputString[i] = getColor(curColor);
			inp[curColor].counts--;
		}
	}
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
		solve();
		cout << outputString << endl;
		//~ if(outputString != "IMPOSSIBLE")
			//~ for(int k = 0 ; k < n-1 ; k++)
			//~ {
				//~ if(outputString[k] == outputString[k+1])
					//~ cout << " test no " << i << " is wrong at location " << k << endl,exit(0);
				//~ if(outputString[0] == outputString[n-1])
					//~ cout << " test no " << i << " is wrong " << endl,exit(0);
			//~ }
		//~ cout << outputString << endl;
	}
	return 0;
}
