#include<bits/stdc++.h>
 
using namespace std;
#define go_baby_go ios::sync_with_stdio(false);cin.tie(NULL);
#define pb push_back
#define pp pop_back
#define f first
#define se second
#define ll long long
const int size=1e6+7;

int main()
{
	go_baby_go
	int t,T,i,j;
	string s;
	cin>>T;
	t=T;
	while(T--)
	{
		cout<<"Case #"<<t-T<<": ";
		cin>>s;
		if(s.size()==1)
		{
			cout<<s<<endl;
			continue;
		}
		for(i=1;i<s.size();i++)
			if(s[i]<s[i-1])break;
		if(i==s.size())
		{
			cout<<s<<endl;continue;
		}
		s='0'+s;
		for(j=s.size()-1;j>0;j--)
		{
			if(j>i)s[j]='9';
			else
			{
				if(s[j]>s[j-1]){s[j]--;break;}
				s[j]='9';
			}
		}
		i=0;
		while(s[i]=='0')i++;
		cout<<s.substr(i)<<endl;
	}
	return 0;
}