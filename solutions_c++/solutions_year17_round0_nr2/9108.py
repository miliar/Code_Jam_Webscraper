#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define lli long long int
lli mexp(lli a,lli b)
{
	if(b==0)
	{
		return 1;
	}
	lli t=mexp(a,b/2);
	if(b%2==0)
	{
		return t*t;
	}
	else
	{
		return t*t*a;
	}
}
int main() {
	// your code goes here
	lli er,t,n,i,j,r,p,d,nd,x,y,z,q,ans;
	lli a1[20],b1[20],flag;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		er=n;
		flag=0;
		ans=0;
		r=n;
		nd=0;
		p=0;
		while(r>0)
		{
			if(r%10==0)
			{
				flag=1;
			}
			a1[nd]=r%10;
			nd++;
			r/=10;
		}
		for(p=0;p<nd/2;p++)
		{
			d=a1[p];
			a1[p]=a1[nd-1-p];
			a1[nd-1-p]=d;
		}
		if(flag)
		{
			x=0;
			for(p=0;p<nd;p++)
			{
				if(a1[p]==0)
				{
					b1[x++]=1;
				}
				else if(x>0)
				{
					b1[x++]=0;
				}
			}
			r=0;
			for(p=0;p<x;p++)
			{
				r*=10;
				r+=b1[p];
			}
			r=n-r;
			y=0;
			z=r;
			while(z>0)
			{
				z/=10;
				y++;
			}
			if(y<nd)
			{
				ans=mexp(10,nd-1)-1;
			}
			n=r;
		}
		if(ans==0)
		{
			r=n;
			nd=0;
			p=0;
			while(r>0)
			{
				if(r%10==0)
				{
					flag=1;
				}
				a1[nd]=r%10;
				nd++;
				r/=10;
			}
			for(p=0;p<nd/2;p++)
			{
				d=a1[p];
				a1[p]=a1[nd-1-p];
				a1[nd-1-p]=d;
			}
			for(p=0;p<nd;p++)
			{
				b1[p]=a1[p];
			}
			sort(b1,b1+nd);
			lli tmp[20];
			for(p=0;p<nd;p++)
			{
				x=b1[p];
				y=a1[p];
				while(x<9)
				{
					x++;
					r=0;
					for(q=0;q<p;q++)
					{
						tmp[q]=b1[q];
					}
					for(q=p;q<nd;q++)
					{
						tmp[q]=x;
					}
					for(q=0;q<nd;q++)
					{
						r*=10;
						r+=tmp[q];
					}
					if(r>er)
					{
						break;
					}
					else
					{
						for(q=0;q<nd;q++)
						{
							b1[q]=tmp[q];
						}
					}
				}
			}
			r=0;
			for(q=0;q<nd;q++)
			{
				r*=10;
				r+=b1[q];
			}
			ans=r;
		}
			cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}