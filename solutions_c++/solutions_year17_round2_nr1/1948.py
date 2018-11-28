#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <iomanip>
using namespace std;
const int MAX_N=2000;
const int INF=1000000000;
pair<long double ,long double> x[MAX_N];
int main() 
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int q1,n,v;
	cin>>q1;
	long double d,a,b,t,ans;
	for (int q=0;q<q1;q++)
	{
		cin>>d>>n;
		for (int i=0;i<n;i++)
		{
			cin>>a>>b;
			x[i]=make_pair(a,b);
		}
		sort(x,x+n);
		reverse(x,x+n);
		t=(d-x[0].first)/x[0].second;
		for (int i=1;i<n;i++)
		{
			t=max(t,(d-x[i].first)/x[i].second);
		}
		ans=d/t;
		cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": "<<ans<<endl;
	}
	return 0;
}