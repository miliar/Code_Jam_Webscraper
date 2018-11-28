#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define pll pair<ll,ll>
int main()
{
	ll test;
	cin>>test;
	for(ll cases=1;cases<=test;cases++)
	{
		ll n,r,o,y,g,b,v;
		cout<<"Case #"<<cases<<": ";
		cin>>n>>r>>o>>y>>g>>b>>v;
		if(g==r&&2*g==n)
		{
			for(int i=0;i<n/2;i++)
			{
				cout<<"GR";
			}
			cout<<"\n";
			continue;
		}
		if(o==b&&2*o==n)
		{
			for(int i=0;i<n/2;i++)
			{
				cout<<"OB";
			}
			cout<<"\n";
			continue;
		}
		if(y==v&&2*v==n)
		{
			for(int i=0;i<n/2;i++)
			{
				cout<<"VY";
			}
			cout<<"\n";
			continue;
		}
		if((g>=r&&g>0)||(o>=b&&o>0)||(v>=y&&v>0))
		{
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		else
		{
			r-=g;
			b-=o;
			y-=v;
			if(r>b+y||b>r+y||y>r+b)
			{
				cout<<"IMPOSSIBLE\n";
				continue;
			}
			ll maxi=r;
			char last='y';
			char maxim='r';
			if(maxi<b)
			{
				maxi=b;
				maxim='b';
			}
			if(maxi<y)
			{
				maxi=y;
				maxim='y';
				last='r';
			}
			ll tot=r+b+y;

			for(int i=0;i<tot;i++)
			{
				if(i==0)
				{
					if(maxim=='y')
					{
						cout<<"Y";
						y--;
						if(y==0)
						{
							for(int i=0;i<v;i++)
								cout<<"VY";
						}
						last='y';
					}
					if(maxim=='r')
					{
						cout<<"R";
						r--;
						if(r==0)
						{
							for(int i=0;i<g;i++)
								cout<<"GR";
						}
						last='r';
					}
					if(maxim=='b')
					{
						cout<<"B";
						b--;
						if(b==0)
						{
							for(int i=0;i<o;i++)
								cout<<"OB";
						}
						last='b';
					}
				}
				else if(last=='r')
				{
					if(b>y||(maxim=='b'&&b==y))
					{
						cout<<"B";
						b--;
						if(b==0)
						{
							for(int i=0;i<o;i++)
								cout<<"OB";
						}
						last='b';
					}
					else
					{
						cout<<"Y";
						y--;
						if(y==0)
						{
							for(int i=0;i<v;i++)
								cout<<"VY";
						}
						last='y';
					}
				}
				else if(last=='b')
				{
					if(r>y||(maxim=='r'&&r==y))
					{
						cout<<"R";
						r--;
						if(r==0)
						{
							for(int i=0;i<g;i++)
								cout<<"GR";
						}
						last='r';
					}
					else
					{
						cout<<"Y";
						y--;
						if(y==0)
						{
							for(int i=0;i<v;i++)
								cout<<"VY";
						}
						last='y';
					}
				}
				else
				{
					if(r>b||(maxim=='r'&&b==r))
					{
						cout<<"R";
						r--;
						if(r==0)
						{
							for(int i=0;i<g;i++)
								cout<<"GR";
						}
						last='r';
					}
					else
					{
						cout<<"B";
						b--;
						if(b==0)
						{
							for(int i=0;i<o;i++)
								cout<<"OB";
						}
						last='b';
					}
				}

			}
			cout<<"\n";
		}
	}
}