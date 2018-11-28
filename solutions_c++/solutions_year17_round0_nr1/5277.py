#include <bits/stdc++.h>
using namespace std;
#define ll long long int
ll k,l;
map <string,int> vis,level;

bool check(string str)
{
	for(int i=0;i<l;i++)
	{
		if(str[i] == '-')
			return false;
	}
	return true;
}

ll bfs(string str)
{
	queue <string> q;
	int left,right;
	q.push(str);
	level[str] = 0;
	vis[str] = 1;
	while(!q.empty())
	{
		string p = q.front();
		//cout<<p<<" "<<level[p]<<endl;
		if(check(p))
		{
			return level[p];
		}
		q.pop();
		for(int i=0;i<=l-k;i++)
		{
			left = i;
			right = left + k - 1;
			for(int j=0;j<l;j++)
			{
				if(j>=left && j<=right)
				{
					if(p[j] == '-')
						str[j] = '+';
					else
						str[j] = '-';
				}
				else
					str[j] = p[j];
			}
			if(vis[str] == 0)
			{
				level[str] = level[p] + 1;
				q.push(str);
				vis[str] = 1;
			}
		}
	}
	return -1;
}

int main()
{
	ll t;
	cin>>t;
	string s;
	for(int z=1;z<=t;z++)
	{
		vis.clear();
		cin>>s>>k;
		l = s.length();
		int count=0;
		for(int i=0;i<l;i++)
		{
			if(s[i] == '-')
				count++;
		}
		ll ans = 1e15;
		ans = bfs(s);
		if(ans == -1)
			cout<<"Case #"<<z<<": "<<"IMPOSSIBLE\n";
		else
			cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}