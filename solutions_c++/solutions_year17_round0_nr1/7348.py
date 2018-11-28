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
int main()
{
	ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
	int t;
	cin>>t;
	for (int _=1;_<=t;_++)
	{
		string s;
		int k,ans=0;
		cin>>s>>k;
		for (int i=0;i<=(int)s.size()-k;i++)
			if (s[i]=='-')
			{		
				for (int j=i;j<i+k;j++)
					if (s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				ans++;
			}
		bool flg=true;
		for (int i=0;i<(int)s.size();i++) if (s[i]=='-') flg=false;
		cout<<"Case #"<<_<<": ";
		if (flg) cout<<ans; 
		else cout<<"IMPOSSIBLE";
		cout<<endl;
	}
	return 0;
}

