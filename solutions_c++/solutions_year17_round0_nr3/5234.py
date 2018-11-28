#include <bits/stdc++.h>
using namespace std;

void test_case(){
	int n, k;
	scanf("%d %d", &n, &k);
	priority_queue<int> pq; pq.push(n);
	
	int a = -1, b = -1;
	for(int i = 1; i <= k; i++){
		int mx = pq.top(); pq.pop();
		a = mx/2;
		if(mx%2 == 1) b = mx/2;
		else b = mx/2 - 1;
		pq.push(a), pq.push(b);
	}
	printf("%d %d\n", a, b);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; k++){
		printf("Case #%d: ", k);
		test_case();
	}
	return 0;
}
