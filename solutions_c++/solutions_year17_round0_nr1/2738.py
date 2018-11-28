//Created by Aashray Agarwal urf maniAC
/*MY ATTITUDE ISN'T BAD,IT'S IN BETA.

YOU BETTER BE NICE TO ME,I COULD BE YOUR BOSS IN A FEW YEARS.

I TURN COFFEE INTO CODE,JUST BE ABLE TO AFFORD MORE COFFEE.*/
#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	freopen("inp1s.in","r",stdin);
	freopen("out1s.txt","w",stdout);
	ll t,i,j,k,fg,ans,p,l;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		string s;
		cin>>s>>k;
		fg=0;
		ans=0;
		l=s.size();
		cout<<"Case #"<<i<<": ";
		for(j=0;j<l-k+1;j++)
		{
			if(s[j]=='-')
			{
				ans++;
				for(p=j;p<j+k;p++)
				{
					if(s[p]=='-')
					s[p]='+';
					else
					s[p]='-';
				}
			}
		}
		for(j=0;j<l;j++)
		{
		    if(s[j]=='-')
		    {
			   fg=1;
			   break;
		    }
		}
		if(fg==0)
		cout<<ans<<"\n";
		else
		cout<<"IMPOSSIBLE\n";
	}
	return 0;
}
