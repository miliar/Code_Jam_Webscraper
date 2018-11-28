#include <bits/stdc++.h>
using namespace std;

void solve() {
	int T;
	scanf("%d", &T);
	getchar();
	for (int i = 0; i < T; i++) {
		int index = 0;
		int number[20];
		int in;
		while ((in = getchar()) != '\n') {
			number[index] = in - '0';
			index++;
		}
		int j = 0;
		while((j + 1 < index) && (*(number + j) <= *(number + j + 1))){
			j++;
		}
		int* relevantindex = number + j;
		//printf("%d\n", j);
		while (relevantindex != (number + index-1)) {
			(*relevantindex)--;
			for(int* itr = relevantindex + 1; itr < number+index; itr++){
				*itr = 9;
			}
			j = 0;
			while((j + 1 < index) && (*(number + j) <= *(number + j + 1))){
				j++;
			}
			relevantindex = number + j;
		}
		long long solution = 0;
		long long power = 1;
		for (int k = index-1; k >= 0; k--){
			solution += power*number[k];
			power *= 10;
		}
		printf("Case #%d: %lld\n", i+1, solution);
}
}

int main() {
	solve();
	return 0;
}