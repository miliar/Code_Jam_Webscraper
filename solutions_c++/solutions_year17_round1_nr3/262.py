#define INF 1<<30
#define PII pair<int,int>
#include <bits/stdc++.h>

using namespace std;

const int N=1<<7;

int T,hd,ad,hk,ak,b,d,s,h,a,ae,he,cas,res=INF;

void Cure()
{
	s++;
	h=hd-ae;
}

void Debuff()
{
	s++;
	ae-=d;
	h-=ae;
}

void Buff()
{
	s++;
	a+=b;
	h-=ae;
}

void Attack()
{
	s++;
	he-=a;
	h-=ae;
}

int main()
{
	for(cin>>T;T--;)
	{
		printf("Case #%d: ",++cas);
		cin>>hd>>ad>>hk>>ak>>b>>d,res=INF;
		
		for(int x=0;x<N;x++)
			for(int y=0;y<N;y++)
			{
				s=0,h=hd,a=ad,ae=ak,he=hk;
				for(int i=0;i<x;i++)
				{
					if(ae-d>=h)
					{
						Cure();
						if(ae-d>=h)
						{
							s=INF;
							break;
						}
					}
					Debuff();
				}
				if(s==INF) continue;

				for(int i=0;i<y;i++)
				{
					if(ae>=h)
					{
						Cure();
						if(ae>=h)
						{
							s=INF;
							break;
						}
					}
					Buff();
				}
				if(s==INF) continue;

				for(;he>0;)
				{
					if(he<=a)
						Attack();
					else
					{
						if(ae>=h)
						{
							Cure();
							if(ae>=h)
							{
								s=INF;
								break;
							}
						}
						Attack();
					}
				}
				res=min(res,s);
			}
		if(res==INF)
			puts("IMPOSSIBLE");
		else
			cout<<res<<endl;
	}
}