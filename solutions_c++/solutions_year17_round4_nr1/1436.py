#include <bits/stdc++.h>
using namespace std;

#define sd(x) 		scanf("%d",&x)
#define su(x) 		scanf("%u",&x)
#define slld(x) 	scanf("%lld",&x)
#define sc(x) 		scanf("%c",&x)
#define ss(x) 		scanf("%s",x)
#define sf(x) 		scanf("%f",&x)
#define slf(x)		scanf("%lf",&x)
#define ll 			long long int
#define mod(x,n) 	(x+n)%n
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define Mod         1000000007

int A[107];

int Count[4];

int DP[101][101][101];
bool is[101][101][101];

int Calc(int one,int two,int three)
{
	if(is[one][two][three])
		return DP[one][two][three];
	is[one][two][three] = true;
	int a,b,c,d,e,f;
	a = b = c = d = e = f = -1;
	if(one>=1 && three>=1)
		a = 1+Calc(one-1,two,three-1);
	if(two>=2)
		b = 1+Calc(one,two-2,three);
	if(one>=2 && two>=1)
		c = 1+Calc(one-2,two-1,three);
	if(two>=1 && three>=2)
		d = 1+Calc(one,two-1,three-2);
	if(one>=4)
		e = 1+Calc(one-4,two,three);
	if(three>=4)
		f = 1+Calc(one,two,three-4);
	if(a==-1 && b==-1 && c==-1 && d==-1 && e==-1 && f==-1)
	{
		if(one>0 || two>0 || three>0)
			DP[one][two][three] = 1;
		else
			DP[one][two][three] = 0;
	} 
	else
	{
		DP[one][two][three] = max(a,max(b,max(c,max(d,max(e,f)))));
	}
	return DP[one][two][three];
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int i,j,k,l,m,n,o,p,q,w,x,y,z,a,b,c,r,tno=1,t,ans;
	// ll i,j,k,l,m,n,o,p,q,w,x,y,z,a,b,c,r,tno=1,t;

	sd(t);
	while(tno<=t)
	{
		sd(n);	sd(p);

		ans = Count[0] = Count[1] = Count[2] = Count[3] = 0;

		for(i=0;i<n;i++)
		{
			sd(A[i]);
			A[i] = A[i]%p;
			Count[ A[i] ]++;
		}

		ans += Count[0];

		if(p==2)
		{
			if(Count[1]%2==0)
				ans += (Count[1]/2);
			else
				ans += (Count[1]/2+1);
		}
		else if(p==3)
		{
			x = min(Count[2],Count[1]);
			ans += (x);
			Count[1]-=x;	Count[2]-=x;
			if(Count[1])	
			{
				if(Count[1]%3==0)
					ans += Count[1]/3;
				else
					ans += Count[1]/3+1;
			}	
			if(Count[2])	
			{
				if(Count[2]%3==0)
					ans += Count[2]/3;
				else
					ans += Count[2]/3+1;
			}				
		}
		else
		{
			ans += Calc(Count[1],Count[2],Count[3]);
		}

		printf("Case #%d: %d\n", tno, ans );

		tno++;
	}
	
	return 0;
}