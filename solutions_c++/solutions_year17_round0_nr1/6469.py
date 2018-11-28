#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
string q,w;
int r,wynik,t;
bool k;
//fstream plik,plik2;
/*long long zamien(string p)
{
	long long g=0;
	for (int i=0;i<p.size();i++)
	{
	g=10*g+((long long)p[i]-48);
	}
	return g;
}*/
int main()
{
	/*fstream plik("plik.in", ios::in );
	fstream plik2("results.out",ios::out);
	if (!plik.good())
	cout<<"NIE";
	if (!plik2.good())
	cout<<"NIE2";
	getline( plik, w );
	t=zamien(w);*/
	cin>>t;
	for (int j=1;j<=t;j++)
	{
	cout<<"Case #"<<j<<": ";
	cin>>q>>r;
	for (int i=0;i<q.size();i++)
	{
	if (q[i]=='-')
	{
		if (i+r<=q.size())
		{
		for (int a=i;a<i+r;a++)
		{
			if(q[a]=='-')
			q[a]='+';
			else
			q[a]='-';
		}
		wynik++;
		}
		else
		{
		cout<<"IMPOSSIBLE"<<endl;
		k=true;
		break;
		}
	}
	}
	if (!k)
	cout<<wynik<<endl;
	k=false;
	wynik=0;
	}
	return 0;
}
