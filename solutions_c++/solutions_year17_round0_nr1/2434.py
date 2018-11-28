#include<bits/stdc++.h>
 
using namespace std;
#define go_baby_go ios::sync_with_stdio(false);cin.tie(NULL);
#define pb push_back
#define pp pop_back
#define f first
#define s second
#define ll long long
const int size=1e6+7;
int ans;
bool check(string s,int k)
{
	int i,j,res=0;
	for(i=0;i<s.size();i++)
	{
		if(s[i]=='-')
		{
			if(i+k>s.size())return true;
			for(j=0;j<k;j++)
				if(s[i+j]=='-')s[i+j]='+';
				else
					s[i+j]='-';
			res++;
		}
	}
	ans=min(res,ans);
	return false;
}
int main()
{
	go_baby_go
	int t,T,k;
	cin>>T;
	string s;
	t=T;
	while(T--)
	{
		cin>>s>>k;
		ans=1e9;
		cout<<"Case #"<<t-T<<": ";
		if(check(s,k))
		{
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		else
		cout<<ans<<endl;
	}
	return 0;
}
