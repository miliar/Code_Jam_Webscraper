#include<bits/stdc++.h>
#define MI 1000000000
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EB emplace_back
using namespace std;

int main()
{
	freopen("out.txt","w",stdout);
	//freopen("in.txt","r",stdin);
	long long t,T,i,j,k,fs,md,ls,mc,n,m,out;
	long long x,y,xx,yy;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld %lld",&n,&m);
		k=m;out=1;
		x=n;y=0;xx=1;yy=0;
		while(k>0)
		{
			// printf("[%lld] %lld has %lld | %lld has %lld\n",k,x,xx,y,yy);
			if(yy==0)
			{
				k-=xx;
				if(k<=0)out=x;
				if(x%2==0)
					yy=xx,x=x/2,y=x-1;
				else
					xx*=2,x=x/2;
			}
			else
			{
				k-=xx;
				if(k<=0){out=x;break;}
				k-=yy;
				if(k<=0){out=y;break;}
				if(x%2==0)
				{
					xx=xx;yy=yy*2+xx;
					x=x/2;y=x-1;
				}
				else
				{
					xx=yy+xx*2;yy=yy;
					x=x/2;y=x-1;
				}
			}
		}
		out--;
		printf("Case #%lld: %lld %lld\n",t,out/2+out%2,out/2);
	}	
}