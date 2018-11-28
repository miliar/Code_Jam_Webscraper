#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iterator>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)
typedef long long ll;

const int INF=1000000000;
const int MAXN=1000000;

struct Solver
{
	string solve()
	{
		ostringstream out;
		int d,n;
		cin>>d>>n;
		vector<pair<int,int> > v;
		REP(i,n)
		{
			int k,s;
			cin>>k>>s;
			v.push_back(make_pair(k,s));
		}
		double l=0;
		double r=1e15;
		REP(T,300)
		{
			double c=(l+r)/2;
			bool ok=true;
			double arrive=d/c;
			REP(i,n)
			{
				ok&=v[i].first+v[i].second*arrive>d;
			}
			if(ok)
				l=c;
			else
				r=c;
		}
		assert(r!=1e15);
		out<<fixed<<setprecision(10)<<l<<endl;
		return out.str();
	}
};

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		printf("Case #%d: %s",test, Solver().solve().c_str());
	return 0;
}
