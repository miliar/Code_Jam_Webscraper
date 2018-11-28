#include <bits/stdc++.h>
using namespace std;
#define rep(a,b,c) for(int a=b;a<c;++a)
#define repeq(a,b,c) for(int a=b;a<=c;++a)
#define debug(x) cerr<<(#x)<<": "<<x<<endl
typedef long long ll;
const int SZ = 4000;
bool neg[SZ], change[SZ];
string s;
int main()
{
	ios::sync_with_stdio(false);
    cin.tie(NULL);
	int T;
	cin >> T;
	repeq(t,1,T)
	{
		int k;
		cin >> s >> k;
		int n = s.length();
		rep(i,0,n)
		{
			neg[i] = s[i]=='-';
			change[i] = false;
		}
		int count = 0;
		bool possible = true;
		bool background = false;
		rep(i,0,n)
		{
			if(change[i])
				background = !background;
			if(background!=neg[i])
				if(i+k<=n)
				{
					count++;
					background = !background;
					if(i+k<n)
						change[i+k]=true;
				}
				else
					possible = false;
		}
		if(possible)
			cout << "Case #" << t << ": " << count << endl;
		else
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
	}	
	return 0;
}
