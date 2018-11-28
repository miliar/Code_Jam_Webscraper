#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	
	
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);


	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin >> T;

	int test = 1;

	while(T--){

		string s;
		cin >> s;

		int k;
		cin >> k;

		int n = s.size();

		int ans = 0;

		bool ok = 1;

		for(int i = 0; i + k <= n; ++i){

			if(s[i] == '+') continue;

			else{

				for(int j = 0; j < k; ++j)
					s[i + j] = (s[i + j] == '-' )? '+' : '-'; 

				ans++;
			}
		}

		for(int i = 0; i < n; ++i){
			if(s[i] != '+'){
				ok = 0;
				break;
			}
		}

		cout << "Case #" << test++ << ": " << (ok ? (to_string(ans)) : "IMPOSSIBLE") << endl;

	}

	return 0;
}