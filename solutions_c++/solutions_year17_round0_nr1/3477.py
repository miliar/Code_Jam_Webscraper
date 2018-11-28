#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		string s;
		int l;
		cin>>s>>l;
		int ans=0;
		for(i=0;i<s.sz;i++)
		{
			if(s[i]=='+')continue;
			if(i+l>s.sz)break;
			ans++;
			for(j=0;j<l;j++)
			{
				if(s[i+j]=='-')s[i+j]='+';
				else s[i+j]='-';
			}
		}
		cout<<"Case #"<<cs<<": ";
		if(i==s.sz)cout<<ans<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
