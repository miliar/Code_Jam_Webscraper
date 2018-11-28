#include <bits/stdc++.h>

using namespace std;

set<pair<long long, pair<long long, long long> > > st;

int main()
{
	freopen("op.txt", "w", stdout);
	long long T,t,i,j,n,k,dis,l,r,mid,a,b;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		st.clear();
		cin>>n>>k;
		st.insert({-n, {2, n+1}});
		k--;
		while(k--)
		{
			l=(*st.begin()).second.first;
			r=(*st.begin()).second.second;
			mid = (l+r)/2;
			st.erase(st.begin());
			st.insert({-(mid-l), {l, mid-1}});
			st.insert({-(r-mid), {mid+1, r}});
		}
		dis = -(*st.begin()).first - 1;
		a = dis - dis/2;
		b = dis/2;

		cout<<"Case #"<<t<<": "<<max(a,b)<<" "<<min(a,b)<<"\n";
	}
}