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
		string n;
		string t;
		cin>>n;
		while(n[0]=='0')
			n=n.substr(1);
		if(is_sorted(n.begin(), n.end()))
			return n;
		ll res=0;
		for(int i=0;i<(int)n.size();i++)
			if(n[i]!='0')
			{
				t=n;
				t[i]--;
				for(int j=i+1;j<(int)t.size();j++)
					t[j]='9';
				if(is_sorted(t.begin(), t.end()))
					res=max(res,atoll(t.c_str()));
			}
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
