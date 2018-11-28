#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r" , stdin);
	freopen("output.txt", "w", stdout);

	int t, tst = 1;
	cin >> t;
	while(t--)
	{
		string st;
		cin >> st;
		while(st.length()!=1 && st[0]=='0') st.erase(st.begin());
		int n = st.length();
		printf("Case #%d: ", tst++);
		if(n==1) {cout << st << endl; continue;}

		for(int i = 0; i<n-1; i++)
			if(st[i]>st[i+1])
			{
				while(st[i]==st[i-1]) {
					i--;
					if(i==0) break;
				}
				st[i]--;
				for(int j = i+1; j<n;j++)
					st[j] = '9';
				break;
			}
		while(st.length()!=1 && st[0]=='0') st.erase(st.begin());
		cout << st << endl;	
	}


	return 0;
}