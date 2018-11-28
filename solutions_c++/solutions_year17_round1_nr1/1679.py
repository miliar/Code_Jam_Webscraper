#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int q = 1; q <= t; q++){
		int r,c;
		cin >> r;
		cin >> c;
		char a[27][27];
		for(int i = 1; i <= r; i++){
			for(int j = 1; j <= c; j++){
				cin >> a[i][j];
			}
		}
		for(int i = 1; i <= r; i++){
			for(int j = 1; j <= c; j++){
				if(a[i][j] != '?'){
					int idxj = 1;
					while (a[i][idxj] != '?' && a[i][idxj] != a[i][j]) idxj++;
					while(idxj <= c && a[i][idxj] == '?' || a[i][idxj] == a[i][j]){
						a[i][idxj] = a[i][j];
						idxj++;
					}
				}
			}
		}
		for(int i = 1; i <= r; i++){
			if(a[i][1] != '?'){
				int idxi = 1;
				while(a[idxi][1] != '?' && a[idxi][1] != a[i][1]) idxi++;
				while(idxi <= r && a[idxi][1] == '?' || a[idxi][1] == a[i][1]){
					for(int j = 1; j <= c; j++){
						a[idxi][j] = a[i][j];
					}
					idxi++;
				}
			}
		}
		cout << "Case #" << q << ":" << endl;
		for(int i = 1; i <= r; i++){
			for(int j = 1; j <= c; j++){
				cout << a[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}