#include<bits/stdc++.h>
#include<iostream>
#include<iomanip>
using namespace std;

ifstream goo;
ofstream gle;

void solve()
{
	double a=0,b,c,d;
	int n;
	goo>>d>>n;
	for(int i=1; i<=n; i++)
	{
		goo>>b>>c;
		b=d-b;
		b=b/c;
		if(b>a) a=b;
	}
	a=d/a;
	gle<<a<<"\n";
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
