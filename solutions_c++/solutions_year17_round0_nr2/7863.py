#include <bits/stdc++.h>
#define PI                3.14159265358979323846264338327950
#define pb                push_back
#define mp                make_pair
#define all(a)            (a).begin(), (a).end()
#define clr(a,h)          memset(a, (h), sizeof(a))
#define F first
#define S second
int in(){int r=0,c;for(c=getchar();c<=32;c=getchar());if(c=='-') return -in();for(;c>32;r=(r<<1)+(r<<3)+c-'0',c=getchar());return r;}

using namespace std;

const int INF = int(1e9 + 7);
typedef pair<int, int>  ii;
typedef vector<int>     vi;
typedef vector<ii>      vii;
typedef long long       ll;
typedef vector<ll>      vll;

string toStr(ll n)
{
	string s;
	while (n > 0)
	{
		s += (char)( n%10 + '0');
		n /= 10;
	}
	reverse(all(s));
	return s;
}

string restar(string s, int pos)
{
	if (s[pos] == '0')
	{
		if (pos == 0)
		{
			s = s.substr(1);
			for (int i = 0; i < s.size(); i++)
			{
				s[i] = '9';
			}
			return s;
		}
		else return restar (s, pos - 1);
	}
	else
	{
		s[pos]--;
		for (int i = pos + 1; i < s.size(); i++)
		{
			s[i] = '9';
		}
		if (s[0] == '0') s = s.substr(1);
		return s;
	}
}

int main()
{
    //std::ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	for (int T = 0; T < t; ++T)
	{
		ll n;
		cin>>n;
		string s = toStr(n);
		while (true)
		{
			bool tidy = true;
			for (int i = 0; i < s.size() - 1; i++)
			{
				if (s[i+1] < s[i])
				{
					s = restar(s, i);
					tidy = false;
					break;
				}
			}
			if (!tidy) continue;
			cout<<"Case #"<<T+1<<": "<<s<<endl;
			break;
		}
	}
    return 0;
}
