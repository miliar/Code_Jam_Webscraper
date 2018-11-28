//In the Name of God
//Let Our Voices Echo
#include<bits/stdc++.h>
using namespace std;
#define X real()
#define Y imag()
typedef long long ll;
typedef double ld; 
typedef complex<ld> point;
const ld eps=1e-9;
const int MAX=1e5+9,MOD=1e9+7;
int t;
int main()
{
	ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
	cin>>t;
	for (int _=1;_<=t;_++)
	{
		multiset<int> s;
		int n,k;
		cin>>n>>k;
		s.insert(n);
		cout<<"Case #"<<_<<": ";
		for (int i=0;i<k;i++)
		{
			int v=*s.rbegin();
			s.erase(s.find(v));
			v--;
			if (i==k-1) cout<<(v+1)/2<<" "<<v/2<<endl;
			s.insert((v+1)/2);
			s.insert(v/2);
		}	
	}
	return 0;
}

