#include<bits/stdc++.h>

using namespace std;

int main()
{
freopen("a.in", "r", stdin);
freopen("b.out", "w", stdout);

string s;
long long int t,sp,T,n,k,ans,ansr,i,j,flag=0;;
cin>>t;


for(T=1;T<=t;T++)
{
	cin>>s>>k;
	flag=0;
	n=s.size();
	ans=0;
	ansr=0;
	
	for(i=0;i<=n-k;i++)
	{
		if(s[i]=='+')
		{}
		else
		{
			s[i]='+';
			
			for(sp=1;sp<k;sp++)
			{
				if(s[i+sp]=='+')
				s[i+sp]='-';
				else
				s[i+sp]='+';
			}
			
			ans++;
		}
		
	}
	
	for(i=1;i<=k;i++)
	if(s[n-i]=='-')
	flag=1;

	printf("Case #%lld: ",T);
	
	if(flag==1)
	cout<<"IMPOSSIBLE";
	else
	{	
		cout<<ans;
	}
	cout<<endl;
}

return 0;
}
