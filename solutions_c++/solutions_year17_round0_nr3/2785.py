//Created by Aashray Agarwal urf maniAC
/*MY ATTITUDE ISN'T BAD,IT'S IN BETA.

YOU BETTER BE NICE TO ME,I COULD BE YOUR BOSS IN A FEW YEARS.

I TURN COFFEE INTO CODE,JUST BE ABLE TO AFFORD MORE COFFEE.*/
#include"bits/stdc++.h"
using namespace std;
#define ll long long int
int main()
{
	freopen("largec.in","r",stdin);
	freopen("out3l.txt","w",stdout);
	ll i,j,k,n,t,test;
	cin>>t;
	for(test=1;test<=t;test++)
	{
	    cout<<"Case #"<<test<<": ";
	    cin>>n>>k;
	    map<ll,ll>mp;
	    map<ll,ll>::iterator it;
	    mp[n]=1;
	    for(i=1;i<k;i++)
	    {
	        it=mp.end();
	        it--;
	        ll val=it->second;
	        j=it->first;
	        if(val<k)
	        {
	            k-=val;
	            mp.erase(it);
	        }
	        else
	        break;
	        if(j%2==0)
	        {
	            mp[j/2]+=val;
	            mp[j/2-1]+=val;
	        }
	        else
	        {
	            mp[j/2]+=(2*val);
	        }
	    }
	    it=mp.end();
	    it--;
	    ll val=it->second;
	    j=it->first;
	    if(j%2==0)
	    {
	        cout<<j/2<<" "<<j/2-1<<"\n";
	    }
	    else
	    {
	        cout<<j/2<<" "<<j/2<<"\n";
	    }
	}
	return 0;
}
