#include <bits/stdc++.h>
using namespace std;

vector<bool> v;
int n, k;
vector<int> L,R,M1,M2;

int f()
{
	
	int mi = 0;
	for(int i=1; i<=n; ++i) if(!v[i])
	{
		int p=i;
		while(!v[p]) --p;
		L[i] = p;
		p = i;
		while(!v[p]) ++p;
		R[i] = p;
		M1[i] = min(i-L[i]-1,R[i]-i-1);
		mi = max(M1[i],mi);
		M2[i] = max(i-L[i]-1,R[i]-i-1);
	}
	int ma = mi;
	for(int i=1; i<=n; ++i) if(!v[i] && M1[i]==mi)
	{
		ma = max(ma,M2[i]);
	}
	for(int i=1; i<=n; ++i) if(!v[i] && M1[i]==mi && M2[i]==ma)
	{
		v[i]=true;
		return i;
	}
	return 0;
}

void solve()
{
	v.clear();
	L.clear();
	R.clear();
	M1.clear();
	M2.clear();
	v.resize(n+2,false);
	L.resize(n+2);
	R.resize(n+2);
	M1.resize(n+2);
	M2.resize(n+2);
	v[0] = v[n+1] = true;
	for(int i=0; i<k-1; ++i) f();
	int last = f();
	cout<<M2[last]<<" "<<M1[last];
}

int main()
{
	int t; cin>>t;
	for(int i=1; i<=t; ++i)
	{
		cout<<"Case #"<<i<<": ";
		cin>>n>>k;
		solve();
		cout<<"\n";
	}
	return 0;
}
