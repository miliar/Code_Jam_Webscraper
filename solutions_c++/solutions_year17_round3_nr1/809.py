#include<bits/stdc++.h>
using namespace std;
//nksheokand
int n,k;
vector<pair<int,int> > V;
bool fnc(pair<int,int> l,pair<int,int> r)
{
	return l.first>r.first;
}
long long str[1001][1001];
long long calc(int i,int j)
{
	if(str[i][j]!=-1)
	return str[i][j];
	if(j<=0 || i>=n)
	return str[i][j]=0;
	long long res;
	if(j==k)
	{
		res=2;
		res*=V[i].first;
		res*=V[i].second;
		res+=(long long)V[i].first*((long long)V[i].first);
		res=max(res+calc(i+1,j-1),calc(i+1,j));
		return str[i][j]=res;
	}
	res=2;
	res*=V[i].first;
	res*=V[i].second;
	return str[i][j]=max(res+calc(i+1,j-1),calc(i+1,j));
}
int main()
{
	fstream in,out;
	in.open("A-large.in");
	out.open("Output.txt");
	int t;
	long long res;
	double r;
	pair<int,int> P;
	in>>t;
	for(int l=1;l<=t;l++)
	{
		in>>n>>k;
		V.clear();
		for(int i=0;i<n;i++)
		{
			in>>P.first>>P.second;
			V.push_back(P);
		}
		sort(V.begin(),V.end(),fnc);
		for(int i=0;i<=n;i++)
		for(int j=0;j<=k;j++)
		{
			str[i][j]=-1;
		}
		res=calc(0,k);
		r=res;
		r*=3.14159265358979;
		out<<"Case #"<<l<<": "<<fixed<<r<<endl;
	}
	in.close();
	out.close();
	return 0;
}
