#include <set>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

typedef long long ll;
struct Solver
{
	Solver()
	{
	}
	string solve()
	{
		string x;
		int k;
		int res,n;
		cin>>x>>k;
		res=0;
		n=x.size();
		for(int i=0;i+k<=n;i++)
			if(x[i]=='-')
			{
				res++;
				for(int j=0;j<k;j++)
					x[i+j]=char('+'+'-'-x[i+j]);
			}
		if(x.find('-')<string::npos)
			return "IMPOSSIBLE";
		else
			return to_string(res);
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		cout<<"Case #"<<test<<": "<<Solver().solve()<<endl;
	return 0;
}
