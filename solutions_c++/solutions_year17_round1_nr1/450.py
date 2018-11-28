#include <bits/stdc++.h>
using namespace std;

int main() {
		freopen("A-small-attempt0.in", "r", stdin);
		freopen("Asmall.txt", "w", stdout);
	int t, tc = 1; cin >> t;
	while(t--){
		int n, m; cin >> n >> m;
		vector<string> a(n);
		vector<bool>empt(m, 1);
		for(int i = 0; i < n; i++){
			cin >> a[i];
			for(int j = 0; j < m; j++){
				if(a[i][j] != '?')
					empt[j] = 0;
			}
		}

		for(int j = 0; j < m; j++){
			if(empt[j])
				continue;
			char first = '?', cur = '?';
			for(int i = 0; i < n; i++){
				if(a[i][j] == '?')
					a[i][j] = cur;
				else{
					cur = a[i][j];
					if(first == '?')
						first = cur;
				}
			}

			for(int i = 0; i < n; i++){
				if(a[i][j] == '?')
					a[i][j] = first;
			}
		}

		for(int i = 0; i < n; i++){
			char first = '?', cur = '?';
			for(int j = 0; j < m; j++){
				if(a[i][j] == '?')
					a[i][j] = cur;
				else{
					cur = a[i][j];
					if(first == '?')
						first = cur;
				}
			}

			for(int j = 0; j < m; j++){
				if(a[i][j] == '?')
					a[i][j] = first;
			}
		}

		cout << "Case #" << tc++ << ":\n";
		for(int i = 0; i < n; i++)
			cout << a[i] << endl;
	}
	return 0;
}
