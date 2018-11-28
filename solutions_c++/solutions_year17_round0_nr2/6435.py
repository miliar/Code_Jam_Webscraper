#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
string n,q;
long long x,t,wynik;
bool k;
fstream plik,plik2;
long long zamien(string p)
{
	wynik=0;
	for (int i=0;i<p.size();i++)
	{
	wynik=10*wynik+((long long)p[i]-48);
	}
	return wynik;
}
int main()
{
	fstream plik("plik.in", ios::in );
	fstream plik2("results.out",ios::out);
	if (!plik.good())
	cout<<"NIE";
	if (!plik2.good())
	cout<<"NIE2";
	getline( plik, q );
	t=zamien(q);
	for (int j=1;j<=t;j++)
	{	
	getline(plik,n);
	x=n.size();
	for (int i=0;i<x-1;i++)
	{
		if ((int)n[i]>(int)n[i+1]&&k==false)
		{
			k=true;
			n[i]=(char)((int)n[i]-1);
			n[i+1]='9';
		}
		else
		if ((int)n[i]>(int)n[i+1])
		{
			n[i+1]='9';
		}

	}
	for (int i=x-1;i>=0;i--)
	{
		if ((int)n[i]<(int)n[i-1])
		{
			n[i-1]=(char)((int)n[i-1]-1);
			n[i]='9';
		}
	}
	k=false;
	plik2<<"Case #"<<j<<": ";
	for (int i=0;i<x;i++)
	{
	if (!k&&n[i]=='0')
	continue;
	else
	{
	plik2<<n[i];
	k=true;
	}
	}
	plik2<<endl;
	k=false;
	}
	return 0;
}
