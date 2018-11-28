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
		int n,ans;
		cin>>n;
		for (int k=n;k>=0;k--)
		{
			bool flg=true;
			int lst=9,tmp=k;
			while (tmp>0) 
			{
				if (tmp%10>lst) flg=false;
				lst=tmp%10;
				tmp/=10;
			}
			if (flg) { ans=k; break;}
		}
		cout<<"Case #"<<_<<": "<<ans<<'\n';
	}
	return 0;
}

