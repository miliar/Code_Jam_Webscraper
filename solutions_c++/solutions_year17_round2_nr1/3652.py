#include<bits/stdc++.h>
//#include<iostream>
#define fr(i,a,b) for(int i=a;i<b;i++)
#define frr(i,a,b) for(int i=b;i>=a;i--)
#define ll long long
#define du double
using namespace std;
struct node
	{
	int k;
	int s;
	};
int comp(struct node a,struct node b)
{
	return a.k>b.k;	
}
main()
{
	int t;
	cin>>t;
	 
	fr(ts,1,t+1)
	{
		ll d,n;
		du max=0,p,a,w;
		cin>>d>>n;
		struct node q[n];
		fr(i,0,n)
		{
			cin>>q[i].k>>q[i].s;
		}
		sort(q,q+n,comp);
		frr(i,0,n-1)
		{
			a=d-q[i].k;
			p=(a)/q[i].s;
			if(max<p)
				max=p;

		}
		w=d/max;
		cout<<"Case #"<<ts<<": "<<setprecision (6) << fixed <<w<<endl;
		
		
		
	}
}