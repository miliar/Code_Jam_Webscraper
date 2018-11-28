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

set<string> vis;

bool check(string s)
{
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '-') return false;
	}
	return true;
}

string formatear(string s)
{
	while (s[0] == '+')
	{
		s = s.substr(1);
	}
	while (s[s.size()-1] == '+')
	{
		s = s.substr(0, s.size() - 1);
	}
	return s;
}

int main()
{
    //std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	for (int T = 0; T < t; ++T)
	{
		string s;
		int k;
		cin>>s>>k;
		s = formatear(s);
		int res = 0;
		while (s.size() >= k)
		{
			res++;
			for (int i = 0; i < k; i++)
			{
				if (s[i] == '+') s[i] = '-';
				else s[i] = '+';
			}
			s = formatear(s);
		}
		cout<<"Case #"<<T+1<<": ";
		if (s.size() == 0) cout<<res<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
		/*
		vis.clear();
		queue<string> qs;
		queue<int> dist;
		qs.push(s);
		dist.push(0);
		vis.insert(s);
		int sol = -1;
		while (!qs.empty())
		{
			s = qs.front();
			//cout<<s<<endl;
			int d = dist.front();
			qs.pop();
			dist.pop();
			bool poss = true;
			for (int i = 0; i < n; i++)
			{
				if (s[i] == '-') poss = false;
			}
			if (poss)
			{
				sol = d;
				break;
			}
			for (int i = 0; i < n - k + 1; i++)
			{
				bool sad = false;
				for (int j = i; j < i + k; ++j)
				{
					if (s[j] == '-') sad = true;
				}
				if (sad)
				{
					for (int j = i; j < i + k; ++j)
					{
						if (s[j] == '+') s[j] = '-';
						else s[j] = '+';
					}
					if (vis.find(s) == vis.end())
					{
						qs.push(s);
						dist.push(d + 1);
						vis.insert(s);
					}
					for (int j = i; j < i + k; ++j)
					{
						if (s[j] == '+') s[j] = '-';
						else s[j] = '+';
					}
				}
			}
		}
		cout<<"Case #"<<T+1<<": ";
		if (sol != -1)
		{
			cout<<sol<<endl;
		}
		else cout<<"IMPOSSIBLE"<<endl;
		*/
	}
    return 0;
}
