#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w+", stdout);
	int T; cin >> T;
	for (int t = 0; t < T; t++){
		long long n,k; cin >> n >> k;
		long long A = 0;
		long long B = n+1;
		long long mid;
		while (k != 1){
			mid = A + (B-A)/2;
			//if ((B - A - 1) % 2 == 0){
				if (k % 2 == 0){
					A = mid;
				}else{
					B = mid;
				}
			/*}else{
				if (k % 2 == 0){
					B = mid;
				}else{
					A = mid;
				}
			}*/
			k = k/2;
		}
		mid = A + (B-A)/2;
		long long Ls = mid - A - 1;
		long long Rs = B - mid - 1;
		if ( Ls > Rs ){
			cout << "Case #" << t+1 << ": " << Ls << " " << Rs << endl;
		}else{
			cout << "Case #" << t+1 << ": " << Rs << " " << Ls << endl;
		}
	}
}