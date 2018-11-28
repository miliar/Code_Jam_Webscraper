#include<iostream>
using namespace std;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, tt, ans, k, i, j;
	string s;
	cin >> t;
	for(tt=1; tt<=t; ++tt)
	{
		cin >> s >> k;
		ans = 0;
		for(i=s.length()-1; i>=0; --i)
		{
			if(s[i]=='-' && i-k+1 >= 0)
			{
				++ans;
				for(j=0; j<k; ++j)
					s[i-j] = s[i-j] == '-' ? '+' : '-';
			}
		}
		cout << "Case #" << tt << ": ";
		if(s.find('-') != string::npos)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}

