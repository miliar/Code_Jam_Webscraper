//Created by Aashray Agarwal urf maniAC
/*MY ATTITUDE ISN'T BAD,IT'S IN BETA.

YOU BETTER BE NICE TO ME,I COULD BE YOUR BOSS IN A FEW YEARS.

I TURN COFFEE INTO CODE,JUST BE ABLE TO AFFORD MORE COFFEE.*/
#include"bits/stdc++.h"
using namespace std;
#define ll long long int
int main()
{
	freopen("inp2s.in","r",stdin);
	freopen("out2s.txt","w",stdout);
	ll t,i,j,k,test,n,newn;
	cin>>t;
	ll a[20];
	for(test=1;test<=t;test++)
	{
		k=19;
		cin>>n;
		cout<<"Case #"<<test<<": ";
		memset(a,0,sizeof a);
		while(n>0)
		{
			a[k]=n%10;
			n=n/10;
			k--;
		}
		for(i=19;i>0;i--)
		{
			if(a[i]>=a[i-1])
			continue;
			else
			{
				a[i-1]--;
				for(j=i;j<=19;j++)
				a[j]=9;
			}
		}
		i=0;
		while(a[i]==0)
		{
		    i++;
		}
		while(i<=19)
		{
		    cout<<a[i];
		    i++;
		}
		cout<<"\n";
	}
	return 0;
}
