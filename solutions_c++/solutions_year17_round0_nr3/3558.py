#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
void calc(LL n,LL k,LL &x,LL &y)
{
	//if (n<k) cout<<"error";
	if (k==0)
	{
		x=y=n;
		return ;
	}
	if (k==1)
	{
		x=(n-1)/2;
		y=n-1-x;
		return ;
	}
	if (n%2==1) calc((n-1)/2,k/2,x,y);
	else
	{
		LL k1=(k-1)/2;
		LL k2=k-1-k1;
		LL x1,y1,x2,y2;
		//if (n/2-1<k1) cout<<n<<"                      "<<k<<endl;
		//if (n/2<k2) cout<<"error2";
		calc(n/2-1,k1,x1,y1);
		calc(n/2,k2,x2,y2);
		if (x1<x2||(x1==x2&&y1<y2))
		{
			x=x1;y=y1;
		}
		else
		{
			x=x2;y=y2;
		}
		/*k1--;k2++;
		if (k1>=0&&k2<=n/2)
		{
			calc(n/2-1,k1,x1,y1);
		    calc(n/2,k2,x2,y2);
		    if (x1<x2||(x1==x2&&y1<y2))
		    {
		    	x2=x1;y2=y1;
		    }
		    if (x<x2||(x==x2&&y<y2))
		    {
		    	x=x2;y=y2;
			}
		}*/
	}
}
int main()
{
	//freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
	int T;cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		LL n,k,x,y;
		scanf("%I64d%I64d",&n,&k);
		calc(n,k,x,y);
		printf("Case #%d: %I64d %I64d\n",ca,y,x);
	}
	return 0;
	//fclose(stdin);fclose(stdout);
}
