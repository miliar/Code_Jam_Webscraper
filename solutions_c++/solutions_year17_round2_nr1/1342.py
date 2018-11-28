#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;
pair<long double,long double> ar[1005];
int t, n;
double d;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>t;
	for(int z=1; z<=t; z++)
	{
		cin>>d>>n;
		ar[0]=make_pair(0, 1e18);
		for(int i=1; i<=n; i++) cin>>ar[i].first>>ar[i].second;
		sort(ar, ar+n+1);
		for(int i=n-1; i>=0; i--)
		{
			ar[i].second=min(ar[i].second, (d-ar[i].first)/((d-ar[i+1].first)/ar[i+1].second));
		}
		cout<<fixed<<"Case #"<<z<<": "<<ar[0].second<<endl;
	}
	return 0;
}