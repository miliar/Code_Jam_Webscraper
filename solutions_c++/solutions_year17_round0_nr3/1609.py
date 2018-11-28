#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std;
long long n,k;
long long odd,even,nownum;
long long nowodd,noweven;
int main()
{
	int T;
	scanf("%d",&T);
	//printf("???\n");
	for(int cas=1;cas<=T;cas++)
	{
		cin>>n>>k;

		odd=0;even=0;
		nowodd=noweven=0;
		if(n%2)
		{
			odd=n;even=0;
			nowodd++;
		}
		else
		{
			odd=0;even=n;
			noweven++;
		}
		nownum=0;
		long long nextnum=1;
		while(nownum+nextnum<k)
		{
			nownum+=nextnum;
			nextnum*=2;
			long long nextodd=0,nexteven=0;
			if((odd/2)%2)
			{
				nextodd+=nowodd*2;
			}
			else nexteven+=nowodd*2;
			nextodd+=noweven;
			nexteven+=noweven;
			if(even!=0)
			{
				if((even/2)%2)
				{
					odd=even/2;
					even=even/2-1;
				}
				else
				{
					odd=even/2-1;
					even=even/2;
				}
			}
			else
			{
				if((odd/2)%2)
				{
					even=0;
					odd=odd/2;
				}
				else
				{
					even=odd/2;
					odd=0;
				}
			}
			noweven=nexteven;
			nowodd=nextodd;
		}
		printf("Case #%d: ",cas);
		long long xx=k-nownum;
		//cerr<<xx<<endl;
		//cerr<<even<<" "<<odd<<endl;
		//cerr<<noweven<<" "<<nowodd<<endl;
		
		if(even>odd)
		{
			if(xx<=noweven)
			{
				cout<<even/2<<" "<<even/2-1<<endl;
			}
			else cout<<odd/2<<" "<<odd/2<<endl;
		}
		else
		{
			if(xx<=nowodd)
				cout<<odd/2<<" "<<odd/2<<endl;
			else
				cout<<even/2<<" "<<even/2-1<<endl;
		}
	}
	return 0;
}