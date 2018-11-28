#include<bits/stdc++.h>
#define	    ll		    long long int
using namespace std;
map<ll,ll> mp;

int main()
{
	ll t,nn,i,j,temp,temp1,l,r,val,val1,x,y,b;
	FILE *wfile;
	
scanf("%lld",&t);
nn=t;
	wfile=fopen("output1.txt","w");
while(t--)
{
	fprintf(wfile,"Case #%lld: ",nn-t);
	temp1=0;
	temp=0;
	mp.clear();
	priority_queue<ll> qi;
	
	scanf("%lld%lld",&l,&r);
	
	qi.push(l);
	mp[l]+=1;

	for(b=r;b>0;)
	{
		val=qi.top();
		val1=mp[val];
		qi.pop();
		if(val%2)
		{
			y=val/2;
			x=y;
		}
		else
		{
			y=val/2;
			x=y-1;
		}
		if(val1>=b)
		{
			temp=y;
			temp1=x;
			break;
		}
		else
		{

			b-=val1;
			if(mp[x]==0)
			{
				qi.push(x);
			}
			mp[x]+=val1;
			if(mp[y]==0)
			{
				qi.push(y);
			}
			mp[y]+=val1;
		}
		
	}
	
	
	
fprintf(wfile,"%lld %lld",temp,temp1);
	fprintf(wfile,"\n");
}
	
	return 0;
}
