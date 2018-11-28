#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t; cin>>t;
	for (int x = 1;x<=t;x++)
	{
	int n,k; cin>>n>>k;
	n += 2;
	bool occ[n+1] = {false};
	int l[n+1],r[n+1];
	occ[1] = occ[n] = true;
	for (int i= 2;i<n;i++)
	{
		l[i] = i-2;
		r[i] = n - i -1;
	}
	int ind;
	for (int j = 1;j<=k;j++)
	{
		int maxi = -1;
		for (int i = 2;i<n;i++)
		{
			if (occ[i]) continue;
			else maxi = max(maxi,min(l[i],r[i]));
		}
		set <int> s;
		for (int i = 2;i<n;i++)
		{
			if (occ[i]) continue;
			else if (min(l[i],r[i])==maxi) s.insert(i);
		}
		if (s.size() > 1)
		{
			maxi = -1;
			for (auto i : s)
			{	
				if (occ[i]) continue;
				else maxi = max(maxi,max(l[i],r[i]));
			}
			vector <int> ex;
			for (auto i : s)
			{	
				if (occ[i]) continue;
				else if (max(l[i],r[i])!=maxi) ex.push_back(i); 
			}
			for (auto i : ex) s.erase(i);
		}
		ind = *(s.begin());
		occ[ind] = true; int prev = 1;
		for (int i = 2;i<n;i++)
		{
			l[i] = i-prev-1;
			if (occ[i]) prev = i;
		}
		prev= n;
		for (int i = n-1;i>1;i--)
		{
			r[i] = prev-i-1;
			if (occ[i]) prev = i;
		}
		//for (int i=2;i<n;i++) cout<<l[i]<<" "<<r[i]<<endl;
	}
	cout<<"Case #"<<x<<": ";
	if (n==k) cout<<0<<" "<<0<<endl;
	else cout<<max(l[ind],r[ind])<<" "<<min(l[ind],r[ind])<<endl;
	}
	return 0;
}
