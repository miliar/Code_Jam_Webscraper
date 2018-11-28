#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;

double tab[1009], r[1009], pi=3.141592653589;

void solve()
{
	int n,k;
	double a,b,c,wyn=0,w;
	vector<double> v;
	goo>>n>>k;
	for(int i=1; i<=n; i++)
	{
		goo>>a>>b;
		r[i]=a;
		b*=pi;
		b*=2;
		b*=a;
		tab[i]=b;
	}
	for(int i=1; i<=n; i++)
	{
		w=r[i]*r[i]*pi;
		w+=tab[i];
		for(int j=1; j<=n; j++) if(j!=i) v.push_back(tab[j]);
		sort(v.begin(), v.end());
		for(int j=1; j<k; j++) w+=v[v.size()-j];
		if(w>wyn) wyn=w;
		v.clear();
	}
	gle<<wyn<<"\n";
	return;
}

int main()
{
	goo.open("C:\\Users\\Mateusz\\Desktop\\Testy\\A-large (4).in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\Testy\\tak.out");
	gle.precision(7);
	gle<<fixed;
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
