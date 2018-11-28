#include <iostream>
using namespace std;

int main(){
	int T; cin >> T;
	for (int i=0;i<T;i++){
		int R, C; cin >> R >> C;
		string a[R];
		for (int j=0;j<R;j++) cin >> a[j];
		
		for (int j=1;j<R;j++){
			for (int k=0;k<C;k++){
				if (a[j][k] == '?') a[j][k] = a[j-1][k];
			}
		}
		for (int j=R-2;j>=0;j--){
			for (int k=0;k<C;k++){
				if (a[j][k] == '?') a[j][k] = a[j+1][k];
			}
		}
		
		for (int j=0;j<R;j++){
			for (int k=1;k<C;k++){
				if (a[j][k] == '?') a[j][k] = a[j][k-1]; 
			}
		}

		for (int j=0;j<R;j++){
			for (int k=C-2;k>=0;k--){
				if (a[j][k] == '?') a[j][k] = a[j][k+1]; 
			}
		}
		cout << "Case #" << i+1 << ":\n";
		for (int j=0;j<R;j++) cout << a[j] << endl;
	}
}
