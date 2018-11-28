#include<iostream>
#include<array>
using namespace std;

int main(){
	int t;
	cin >> t;
	int *output;
	output = new int[t];
	for (int k = 0; k < t; k++){
		getchar();
		unsigned long long n;
		cin >> n;
		unsigned long long out = 0;
		for (long long i = n; i >= 0; i--){
			int mae = 10;
			bool o = true;
			int nn[20] = { 0 };
			int count = 0;
			for (long long j = 1; j <= i; j *= 10)
				nn[count++] = (i / j) % 10;
			nn[count] = 11;
			for (int j = 0; j < 20 && nn[j] != 11; j++){
				if (mae >= nn[j])
					mae = nn[j];
				else
					o = false;
			}
			if (o){
				output[k] = i;
				break;
			}
		}
	}
	for (int i = 0; i < t; i++){
		cout << "Case #" << i + 1 << ": " << output[i] << "\n";
	}
}