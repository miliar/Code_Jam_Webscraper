#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int T = 0; T < t; T++)
	{
		cout << "Case #" << T+1 << ": ";
		string s;
		cin >> s;
		int n = s.size();
		for (int i=0; i+1<n; i++)
			if (s[i] > s[i+1])
			{
				int j = i;
				while (j >= 0 && s[i] == s[j])
					j--;
				j++;
				s[j]--;
				for (int k=j+1; k<n; k++)
					s[k] = '9';
				break;
			}
		for (int i=0; i<n; i++)
			if (s[i] != '0')
				cout << s[i];
		cout << "\n";
	}


	return 0;
}
