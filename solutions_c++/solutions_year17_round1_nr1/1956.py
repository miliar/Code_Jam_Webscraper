#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


int main(int argc, char const *argv[])
{
	
	
	#ifdef Cyborg1o1
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif	

	cin.sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;

	for(int tt = 1; tt <= t; ++tt){

		string s[26];

		int r, c;
		cin >> r >> c;

		for(int x = 0; x < r; ++x)
			cin >> s[x];


		cout << "Case #" << tt << ": " << endl;

		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				if(s[i][j] == '?')
				{
					if(j + 1 < c && s[i][j + 1] != '?')
						s[i][j] = s[i][j + 1];
					else if(j - 1 >= 0 && s[i][j - 1] != '?')
						s[i][j] = s[i][j - 1];
				}
			}
			for(int j = c - 1; j >= 0; --j){
				if(s[i][j] == '?')
				{
					if(j + 1 < c && s[i][j + 1] != '?')
						s[i][j] = s[i][j + 1];
					else if(j - 1 >= 0 && s[i][j - 1] != '?')
						s[i][j] = s[i][j - 1];
				}
			}
		}


		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				if(s[i][j] == '?'){
					int tmp = i;
					while(tmp < r && s[tmp][j] == '?')
						tmp++;

					if(tmp < r)
						s[i][j] = s[tmp][j];
				}
				if(s[i][j] == '?'){
					int tmp = i;
					while(tmp >= 0 && s[tmp][j] == '?')
						tmp--;

					if(tmp >= 0)
						s[i][j] = s[tmp][j];
				}
				
			}
			cout << s[i] << endl;
		}

	}

	return 0;
}