#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A_lar","w",stdout);
	int t;
	cin >> t;
	for(int p=1;p<=t;p++){
		int r,c;
		cin >> r >> c;
		char a[r][c];
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin >> a[i][j];
			}
		}
		char aux = '?';
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(a[i][j]=='?' && aux!='?'){
					a[i][j] = aux;
				}
				else if(a[i][j]!='?'){
					aux = a[i][j];
				}
			}
			aux = '?';
			for(int j=c-1;j>=0;j--){
				if(a[i][j]=='?' && aux!='?'){
					a[i][j] = aux;
				}
				else if(a[i][j]!='?'){
					aux = a[i][j];
				}
			}
			aux = '?';
		}
		//cout << "aple" << endl;
		for(int i=0;i<c;i++){
			for(int j=0;j<r;j++){
				if(a[j][i]=='?' && aux!='?'){
					a[j][i] = aux;
				}
				else if(a[j][i]!='?'){
					aux = a[j][i];
				}
			}
			aux = '?';
			for(int j=r-1;j>=0;j--){
				if(a[j][i]=='?' && aux!='?'){
					a[j][i] = aux;
				}
				else if(a[j][i]!='?'){
					aux = a[j][i];
				}
			}
			aux = '?';
		}

		cout << "Case #" << p << ":" << endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout << a[i][j];
			}
			cout << endl;
		}

	}

}

