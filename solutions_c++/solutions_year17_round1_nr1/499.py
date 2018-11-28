#include <bits/stdc++.h>
using namespace std;

int t,r,c;
char a[30][30];

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	for (int tc=1;tc<=t;tc++){
		cout << "Case #" << tc << ":\n";
		cin >> r >> c;
		for (int i=1;i<=r;i++){
			int last=-1;
			for (int j=1;j<=c;j++){
				cin >> a[i][j];
				if (a[i][j]!='?'){
					for (int k=j-1;k;k--){
						if (a[i][k]!='?') break;
						a[i][k]=a[i][j];
					}
					last=j;
				}
			}
			if (last!=-1){
				for (int k=last+1;k<=c;k++){
					a[i][k]=a[i][last];
				}
			}
		}
		for (int i=1;i<=c;i++){
			int last=-1;
			for (int j=1;j<=r;j++){
				if (a[j][i]!='?'){
					for (int k=j-1;k;k--){
						if (a[k][i]!='?') break;
						a[k][i]=a[j][i];
					}
					last=j;
				}
			}
			assert (last!=-1);
			for (int k=last+1;k<=r;k++){
				a[k][i]=a[last][i];
			}
		}
		for (int i=1;i<=r;i++){
			for (int j=1;j<=c;j++){
				cout << a[i][j];
			}
			cout << "\n";
		}
	}
}
