#include <bits/stdc++.h>
#define  mp make_pair
#define pb push_back
#define pf push_front
#define pp pop_back
#define ppf pop_front
#define fi first
#define se second
#define maxn 1000005

typedef long long ll;
using namespace std;
#define pi pair<int,int>


/*struct node
{
	int i;
 
	bool friend operator < (node a,node b)
	{
		return w[a.i]>w[b.i];
	}
};
priority_queue<node>pq;*/

int a[maxn],b[maxn];
int main()
{
	ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
	int t;
	cin>>t;
	int c = 1;
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		//cout<<s<<" "<<k<<endl;
		int cnt = 0;
		int sz = s.size();
		int flag= 0;
		for(int i=0;i<sz;i++)
		{
			if(s[i]=='-')
			{
				if(i+k-1>=sz)
				{
					break;
					flag = 1;
				}
				for(int j=i;j<i+k;j++)
				{
					if(s[j]=='-') s[j] = '+';
					else s[j] = '-';
				}
				cnt++;
			}
		}
		if(flag) cout<<"Case #"<<c<<":"<<" "<<"IMPOSSIBLE"<<endl;
		else
		{
			for(int i=0;i<sz;i++)
			{
				if(s[i]=='-')
				{
					flag = 1;
					break;
				}
			}
			if(flag) cout<<"Case #"<<c<<":"<<" "<<"IMPOSSIBLE"<<endl;
			else cout<<"Case #"<<c<<":"<<" "<<cnt<<endl;
		}
		c++;
	}
	return 0;
}