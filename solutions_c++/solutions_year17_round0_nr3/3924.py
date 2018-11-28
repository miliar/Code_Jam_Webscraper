#include <bits/stdc++.h>
using namespace std;
#define ll int
#define N ((ll)110)
#define M ((ll)1010)

ll t,n,k;
ifstream fin("input.in");
ofstream fout("output.txt");

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);
	fin>>t;
	for(int q=1;q<=t;q++)
	{
		fin>>n>>k;
		set <pair<ll,ll> > s;s.insert({-n,0});
		fout<<"Case #"<<q<<": ";
		for(int i=0;i<k;i++)
		{
			pair <ll,ll> x=*s.begin();x.first*=-1;
			s.erase(s.begin());
			s.insert({-(x.first-1)/2,x.second});
			s.insert({-x.first/2,x.second+(x.first-1)/2+1});
			if(i==k-1)fout<<x.first/2<<" "<<(x.first-1)/2<<"\n";
		}
	}
	return 0;
}
