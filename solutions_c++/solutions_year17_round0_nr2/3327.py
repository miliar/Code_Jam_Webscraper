#include <iostream>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int digits[20];
		for (int j = 0; j < 20; ++j)
		{
			digits[j] = -1;
		}

		long long N;
		long long M;
		cin >> N;
		M = N;
		int j = 0;
		while (N > 0){
			digits[j] = N % 10;
			N /= 10;
			j++;
		}
		j--;
		int j2 = j;
		long long res = 0;
		bool hasDescending = false;
		if (j == 0){
			cout << "Case #" << i << ": " << digits[0] << endl;
		} else{
			while (j > 0 && !hasDescending){
				if (digits[j] > digits[j-1]){
					hasDescending = true;
				}
				j--;
			}

			if (hasDescending){

				int k = j;
				while (k >= 0){
					digits[k] = 9;
					k--;
				}

				j++;
				while (j <= j2){
					digits[j] = (digits[j] - 1) % 10;
					if (j == j2){
						break;
					}
					if (digits[j] != 9){
						if (digits[j] < digits[j+1]){
							digits[j] = 9;
						} else{
							break;
						}
					}
					j++;
				}

				res = 0;
				k = 0;
				long long mult = 1;
				while (digits[k] != -1){
					res += digits[k] * mult;
					mult *= 10;
					k++;
				}
			} else{
				res = M;
			}

			cout << "Case #" << i << ": " << res << endl;
		}
	}
	return 0;
}