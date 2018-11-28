#include <bits/stdc++.h>

using namespace std;

int main (){

	freopen("in.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;

	for (int t = 1; t <= T; t++){

		string s, ans;
		cin >> s;
		int n = s.size();

		reverse (s.begin(), s.end());


		for (int i = 0; i < n - 1; i++){
			if (s[i] - '0' < s[i+1] - '0'){
				s[i+1]--;
				ans+='9';
			}
			else ans+=s[i];
		}

		if (s[n-1] > '0') ans+=s[n-1];

		reverse(ans.begin(), ans.end());

		for (int i = 0; i < ans.size(); i++)
			if (ans [i] == '0') ans[i] = '9';

		for (int i = 0; i < ans.size() - 1; i++)
			if (ans [i] > ans [i+1])
				ans[i+1] = '9';

		cout << "Case #" << t << ": " << ans << endl;


	}


}
