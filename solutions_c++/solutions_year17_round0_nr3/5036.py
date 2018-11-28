#include <bits/stdc++.h>
#define ll long long int

using namespace std;

multiset< pair<int, int> , greater< pair<int, int> > > s;

int main()
{
	ios_base::sync_with_stdio(false);
	int t,n,k,mini,maxi;
	cin>>t;
	for(int loop=1;loop<=t;loop++)
	{
		s.clear();
		cin>>n>>k;
		n--;
		s.insert(make_pair(n/2, n-n/2));
		while(k--)
		{
			mini = s.begin()->first;
			maxi = s.begin()->second;
			mini--;
			maxi--;
			s.erase(s.begin());
			s.insert(make_pair(mini/2, mini-mini/2));
			s.insert(make_pair(maxi/2, maxi-maxi/2));
		}
		cout<<"Case #"<<loop<<": "<<maxi+1<<" "<<mini+1<<"\n";
	}
	return 0;
}