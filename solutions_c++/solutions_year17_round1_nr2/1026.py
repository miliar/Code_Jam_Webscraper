#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;

int tab[100];
priority_queue<int, vector<int>, greater<int> > v[100];

void solve()
{
	int n,p,a,b,c,d,e,s=0;
	goo>>n>>p;
	for(int i=1; i<=n; i++) goo>>tab[i];
	for(int i=1; i<=n; i++)
	{
		while(!v[i].size()==0) v[i].pop();
		for(int j=1; j<=p; j++)
		{
			goo>>a;
			v[i].push(a);
		}
	}
	a=1;
	while(true)
	{
		b=1;
		for(int i=1; i<=n; i++)
		{
			if(v[i].size()==0)
			{
				b=-1;
				break;
			}
			c=0.9*a*tab[i];
			d=1.1*a*tab[i];
			e=v[i].top();
			while(e<c)
			{
				v[i].pop();
				if(v[i].size()==0)
				{
					b=-1;
					break;
				}
				e=v[i].top();
			}
			if(e>d) b=0;
		}
		if(b==-1) break;
		if(b==1)
		{
			s++;
			for(int i=1; i<=n; i++) v[i].pop();
		}
		else a++;
	}
	gle<<s<<"\n";
	return;
}

int main()
{
	goo.open("C:\\Users\\Mateusz\\Desktop\\Testy\\B-large (2).in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\Testy\\tak.out");
	int t;
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
