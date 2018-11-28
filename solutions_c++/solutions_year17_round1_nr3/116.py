#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
static ll turns(ll Hk,ll Ad,ll B)
{
	ll res=Hk;
	for(ll k=0;k<res;k++)
	{
		ll sum=(k*B+Ad);
		if(Hk%sum==0)
			res=min(res,k+(Hk/sum));
		else
			res=min(res,k+1+(Hk/sum));
	}
	return res;
}
static ll val(ll Hd,ll Ak,ll D,ll count,ll t)
{
	ll h=Hd;
	int res=0;
	while(count>0)
	{
		if(h-Ak+D<=0)
		{
			h=Hd-Ak;
			res++;
			if(h-Ak+D<=0)
				return -1;
			continue;
		}
		Ak-=D;
		h-=Ak;
		res++;
		count--;
	}
	while(t>0)
	{
		if(t==1)
			return res+1;
		if(h-Ak<=0)
		{
			h=Hd-Ak;
			res++;
			if(h-Ak<=0)
				return -1;
			continue;
		}
		t--;
		h-=Ak;
		res++;
	}
	return res;
}
int main() {
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("C-small-attempt0.in");
	ll t;
	fin >> t;
	for(ll h=0;h<t;h++)
	{
		ll Hd,Ad,Hk,Ak,B,D;
		fin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		ll t=turns(Hk,Ad,B);
		fout << "Case #" << h+1 << ": ";
		if(t==1)
		{
			fout << t << endl;
			continue;
		}
		int res=-1;
		for(int i=0;i<=Ak;i++)
		{
			int v=val(Hd,Ak,D,i,t);
			if(res==-1||(v<res&&(v!=-1)))
				res=v;
		}
		if(res==-1)
			fout << "IMPOSSIBLE" << endl;
		else
			fout << res << endl;
	}
	fout.close();
	fin.close();
    return 0;
}
