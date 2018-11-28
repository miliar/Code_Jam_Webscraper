#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define max 100010
char a[max];
char ans[max];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ans4.txt","w",stdout);
	ll t;
	cin>>t;
	ll  kase=1;
	while(t--)
	{
	
		cin>>a;
		ll len=strlen(a);
		ll k;
		cin>>k;
		ll i,j;
		i=0;
		j=0;
		ll cnt=0;
		bool flag=true;
		while(i<len)
		{
			if(a[i]=='+')
			{
			  ans[j]=a[i];
			  i++;
			  j++;	
			}
			else
			{
				ll test=k;
				ll p=0;
				for(p=0;p<test&&(i+p)<len;p++)
				{
					if(a[i+p]=='-')
					a[i+p]='+';
					else
					a[i+p]='-';
				}
				cnt++;
				if(p!=test)
				{
					flag=false;
					break;
				}
			}
		}
			cout<<"Case #"<<kase<<": ";
		kase++;
		if(flag==false)
		cout<<"IMPOSSIBLE\n";
		else
		{
			for(ll p=0;p<len;p++)
			{
				if(ans[p]=='-')
			{
				flag=false;
				break;
			}
			}
			if(flag==false)
				cout<<"IMPOSSIBLE\n";
				else
				cout<<cnt<<endl;
		}
		
		
	}
}
