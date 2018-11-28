#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	int t; cin>>t;
	for (int i = 0; i < t; i += 1)
	{
		string s; cin>>s;
		int n = s.length();
		int f = 0;
		cout<<"Case #"<<(i+1)<<": ";
		for(int j = n - 1; j > 0; --j)
		{
			if(s[j] < s[j - 1])
			{
				for(int k = j; k < n; ++k) s[k] = '9';
				s[j - 1] = s[j - 1] - 1;
				if(s[j - 1] == '0') ++j;
            }
			while(s[j] == '0')
			{
				f = 1;
				j--;
			}
            if(f)
            {
				s[j] = s[j] - 1;
				for(int k = j + 1; k < n; ++k) s[k] = '9';
				if(s[j] == '0') ++j;
				f = 0;
			}
		}
		ll sol = stoll(s);		
		cout<<sol<<"\n";
	}
	return 0;
}

