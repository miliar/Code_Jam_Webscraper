#include <iostream>

using namespace std;

int arr[100];

long long pow(int k){
	long long res = 1;
	while(k--){
		res *= 10;
	}
	return res;
}

long long tidy(int pp){
	long long F = 0;
	for(int check = pp; check > 1; --check){
		if(arr[check] > arr[check-1]){
			F /= pow(pp-check); 
			F = 10*F+arr[pp]-1; --pp;
			for(; pp > 0; --pp){
				F = F*10+9;
			} return F;
		} else {
			F = F*10+arr[check];
			if(arr[check] < arr[check-1]) pp=check-1;
		}
	}

	F = F*10+arr[1];
	return F;
}

void ll_arr(long long x){
	arr[0] = 0;
	for(int i = 1; x > 0; x /= 10, ++i){
		++arr[0]; 
		arr[i] = x%10;
	}
}

int main(){
	int T; cin >> T;
	for(int i = 1; i < T+1; ++i){
		long long N; cin >> N;
		ll_arr(N);
		cout << "Case #" << i << ": " << tidy(arr[0]) << endl;
	}

	return 0;
}