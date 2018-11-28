#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <stdio.h>
using namespace std;
int t, n, k;
long double p, arr[55];
int main(){
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("Csmallout.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d%d", &n, &k);
		scanf("%Lf", &p);
		for (int j = 0; j < n; j++){
			scanf("%Lf", &arr[j]);
		}
		sort(arr, arr + n);
		long double cursum = arr[0];
		for (int j = 1; j < n; j++){
			if (cursum + p <= arr[j]*j){
				for (int l = 0; l < j; l++){
					arr[l] = (cursum + p)/j;
				}
				p = 0;
				break;
			}
			cursum += arr[j];
		}
		if (p != 0){
			for (int j = 0; j < n; j++){
				arr[j] = (cursum + p)/n;
			}
		}

		long double answer = 1;
		for (int j = 0; j < n; j++){
			answer *= arr[j];
		}
		printf("Case #%d: %.9Lf\n", i + 1, answer);
	}
}
