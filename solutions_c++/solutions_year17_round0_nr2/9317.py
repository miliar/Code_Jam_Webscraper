#include <bits/stdc++.h>
using namespace std;

int arr[18];

int main(){
	int qt;
	scanf("%d", &qt);

	long long x;
	for (int q = 0; q < qt; q++){
		printf("Case #%d: ", q+1);
		scanf("%lld", &x);

		for (int i = 0; i < 18; i++){
			arr[i] = x%10;
			x/=10;
		}

		int ans = -1;
		for (int i = 0; i < 17; i++){
			if(arr[i] < arr[i+1]){
				arr[i+1]--;
				ans = i;
			}
		}

		bool zero = true;
		for (int i = 17; i --> 0;){
			if(i <= ans){
				printf("9");
				zero = false;
			}else if(arr[i] == 0 && zero){
				continue;
			}else{
				printf("%d", arr[i]);
				zero = false;
			}
		}
		if(zero) printf("0");
		printf("\n");
	}
}