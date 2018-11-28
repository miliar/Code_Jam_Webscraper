#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
	int t; cin >> t;
	for (int i=1;i<=t;i++){
		int N,P; cin >> N >> P;
		int R[N];
		for (int j=0;j<N;j++) cin >> R[j];
		int Q[N][P];
		for (int j=0;j<N;j++)
			for (int k=0;k<P;k++) cin >> Q[j][k];
		
		if (N == 1){
			int ans = 0;
			for (int j=0;j<P;j++){
				int x = Q[0][j];
				int l = 10*x/11/R[0];
				if ((10*x) % (11*R[0]) != 0) l++;
				int r = 10*x/9/R[0];
				if (r>=l) ans++;
			}
			cout << "Case #" << i << ": " << ans << endl;
		}
		
		if (N == 2){
			int ans = 0;
			int ord[P];
			for (int j=0;j<P;j++) ord[j] = j;
			do {
				int tans = 0;
				for (int j=0;j<P;j++){
					int x = Q[0][j];
					int l = 10*x/11/R[0];
					if ((10*x) % (11*R[0]) != 0) l++;
					int r = 10*x/9/R[0];
				
					if (r < l) continue;
					
					int y = Q[1][ord[j]];
					int l2 = 10*y/11/R[1];
					if ((10*y) % (11*R[1]) != 0) l2++;
					int r2 = 10*y/9/R[1];
					
					if (r2 <l2) continue;
					
					if (r2 < l || r < l2) continue;
					tans++;
				}
				if (ans < tans) ans = tans;
			} while (next_permutation(ord,ord+P));
			cout << "Case #" << i << ": " << ans << endl;
		}
	}
}
