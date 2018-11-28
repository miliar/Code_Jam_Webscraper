#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int T; cin >> T;
	for (int t=0;t<T;t++){
		int N, P; cin >> N >> P;
		int cn[P];
		for (int i=0;i<P;i++) cn[i] = 0;
		for (int i=0;i<N;i++) {
			int x;
			cin >> x;
			cn[x%P]++;
		}
	//	cout << cn[1] << cn[2] << cn[3] << endl;
		int ans = cn[0];
		if (P == 2){
			ans += cn[1]/2;
			if (cn[1]%2) ans++;
		}
		if (P == 3){
			int m = min(cn[1], cn[2]);
			ans += m; cn[1] -= m; cn[2] -= m;
			ans += cn[1]/3 + (int)(cn[1]%3 != 0);
			ans += cn[2]/3 + (int)(cn[2]%3 != 0);
		}
		if (P == 4){
			int m = min(cn[1], cn[3]);
			ans += m; cn[1] -= m; cn[3] -= m;
			while (cn[1]>=2 && cn[2]>0){
				cn[1]-= 2;
				cn[2]--; ans++;
			}
			while (cn[3]>=2 && cn[2]>0){
				cn[3]-= 2;
				cn[2]--; ans++;
			}
			while (cn[2] >= 2){
				cn[2] -= 2; ans++;
			}
			while (cn[1] >= 4){
				cn[1]-=4; ans++;
			}
			while (cn[3] >= 4){
				cn[3]-=4; ans++;
			}
			if (cn[2] || cn[1] || cn[3]) ans++;
		}
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
}
