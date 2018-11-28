#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, tst = 1;
	cin >> t;
	while(t--)
	{
		int k;
		string st;
		cin >> st >> k;
		int n = st.length();
		int cnt = 0;
		for(int i = 0; i<n-k+1; i++)
		{
			if(st[i]=='-'){
				cnt++;
				for(int j = i; j<i+k; j++)
					st[j] = st[j]=='-' ? '+' : '-';
			}
		}
		int f = 0;
		for(int i = 0; i<n; i++)
			if(st[i]=='-') f = 1;
		printf("Case #%d: ", tst++);
		if(!f) cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;

}