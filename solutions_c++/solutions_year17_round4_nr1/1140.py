#include <iostream>

using namespace std;

int G[105];

int main(){
	int T;
	cin >> T;
	
	for(int t = 0; t < T; t++){
		int N,P;
		cin >> N >> P;
		for(int i = 0; i < N; i++){
			cin >> G[i];
		}
		
		int num0 = 0;
		int num1 = 0;
		int num2 = 0;
		int num3 = 0;
		for(int i = 0; i < N; i++){
			if (G[i] % P == 0){
				num0++;
			} else if (G[i] % P == 1){
				num1++;
			} else if (G[i] % P == 2){
				num2++;
			} else {
				num3++;
			}
		}
		int ans = num0;
		if (P == 2){
			ans += num1 / 2 + (num1 % 2);
		} else if (P == 3){
			int m = min(num1, num2);
			num1 -= m;
			num2 -= m;
			ans += m;
			
			int l = 0;
			if (num1 % 3 > 0 || num2 % 3 > 0){
				l++;
			}
			
			ans += num1 / 3 + num2 / 3 + l;
		} else {
			int m = min(num1, num3);
			num1 -= m;
			num3 -= m;
			ans += m;
			ans += num2 / 2;
			num2 -= (num2 / 2) * 2;
			if (num2 > 1){
				cout << "WTF" << endl;
			}
			if (num2 > 0){
				if (num1 > 1){
					num1 -= 2;
					ans ++;
					num2--;
				}
				if (num3 > 1){
					num3 -= 2;
					ans++;
					num2--;
				}
			}
			ans += num1 / 4 + num3 / 4;
			if (num1 % 4 > 0 || num3 % 4 > 0 || num2 % 4 > 0){
				ans++;
			}
		}
		if (ans == 0){
			for(int i = 0; i < N; i++){
				cout << N << " " << P << endl;
				cout << G[i] << " ";
			}
		}
		cout << "Case #" << t + 1<< ": " << ans << endl;
	}
}