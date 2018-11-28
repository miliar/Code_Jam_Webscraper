#include <bits/stdc++.h>
using namespace std;

const int N = 2e3 + 5;

int arr[N];
char str[N];

int main(){
	int t, tt = 0;
	scanf("%d", &t);

	while(t--){
		int k, n, ans = 0;
		scanf("%s %d", str, &k);

		n = strlen(str);

		memset(arr, 0, sizeof(arr));

		for(int i=0; i<=n-k; i++){
			if(i == 0)
				arr[i] = 0;
			else
				arr[i] += arr[i-1];

			if(arr[i]%2 == 0){
				if(str[i] == '+')
					continue;
				else{
					arr[i] += 1;
					arr[i+k] -= 1;
					ans += 1;
				}
			}
			else{
				if(str[i] == '-')
					continue;
				else{
					arr[i] += 1;
					arr[i+k] -= 1;
					ans += 1;
				}
			}
		}

		for(int i=n-k+1; i<n; i++)
			arr[i] += arr[i-1];

		bool can = true;

		for(int i=0; i<n; i++){
			if((str[i] == '+' && arr[i] % 2 == 1) || (str[i] == '-' && arr[i] % 2 == 0))
				can = false;
		}

		printf("Case #%d: ", ++tt);

		if(can == false)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
}