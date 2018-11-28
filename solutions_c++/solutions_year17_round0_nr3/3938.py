#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	scanf(" %d", &T);

	for (int t = 0; t < T; t++){
		int n, m;
		scanf(" %d %d", &n, &m);

		priority_queue<int> pq;
		pq.push(n);

		for (int i = 0; i < m - 1; i++){
			int top = pq.top();pq.pop();
			if (top % 2 == 1){
				top /= 2;
				pq.push(top);
				pq.push(top);
			}
			else{
				top /= 2;
				pq.push(top);
				pq.push(top - 1);
			}
		}

		int top = pq.top();
		if (top % 2 == 1){
			printf("Case #%d: %d %d\n", t + 1, top / 2, top / 2);	
		}
		else{
			int next = 0;
			if (top / 2 == 0){
				next = 0;
			}
			else
				next = top / 2 - 1;
			printf("Case #%d: %d %d\n", t + 1, top / 2, next);
		}

	}
	return 0;
}
