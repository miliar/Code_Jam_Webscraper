#include<bits/stdc++.h>
using namespace std;
//nksheokand
bool fnc(pair<int,int> l,pair<int,int> r)
{
	return l.first<r.first;
}
vector<pair<int,int> > V;
int main()
{
	fstream in,out;
	in.open("A-large.in");
	out.open("Output.txt");
	int t,d,n,k,s;
	long double r,rt,st;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>d>>n;
		V.clear();
		for(int i=0;i<n;i++)
		{
			in>>k>>s;
			V.push_back(make_pair(k,s));
		}
		//sort(V.begin(),V.end(),fnc);
		r=(long double)(d-V[n-1].first)/(long double)(V[n-1].second);
		for(int i=n-2;i>=0;i--)
		{
			r=max(r,(long double)(d-V[i].first)/(long double)(V[i].second));
		}
		r=(long double)(d)/r;
		out<<"Case #"<<l<<": "<<fixed<<r<<endl;
	}
	in.close();
	out.close();
	return 0;
}

