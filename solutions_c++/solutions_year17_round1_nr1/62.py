#include<bits/stdc++.h>

using namespace std;

const int MAXN = 25 + 10;

int n, m;
string s[MAXN];

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> n >> m;
		for (int i = 0; i < n; i++){
			cin >> s[i];
			bool found = 0;
			char lst;
			for (int j = 0; j < m; j++){
				found |= s[i][j] != '?';
				if (found){
					lst = s[i][j];
					break;
				}
			}

			if (found){
				for (int j = 0; j < m; j++){
					if (s[i][j] != '?') lst = s[i][j];
					s[i][j] = lst;
				}
			}
		}

		string lst;
		for (int i = 0; i < n; i++)
			if (s[i][0] != '?'){
				lst = s[i];
				break;
			}
		for (int i = 0; i < n; i++){
			if (s[i][0] != '?') lst = s[i];
			s[i] = lst;
		}

		cout << "Case #" << w << ": \n";
		for (int i = 0; i < n; i++)
			cout << s[i] << "\n";
	}
	return 0;
}
