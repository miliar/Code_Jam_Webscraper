#include <bits/stdc++.h>
using namespace std;
int main () {

	int t, co = 0; 
	cin>>t; 
	while(t--) {
		int n, k; 
		scanf("%d %d", &n, &k);
		priority_queue<int> Q; 
		Q.push(n); k--;
		while(k--) {
			int next = Q.top(); Q.pop();
			Q.push(next / 2);
			if(next & 1) 
				Q.push(next/2);
			else Q.push(next / 2 - 1);
		} int fk = Q.top();
		printf("Case #%d: %d ", ++co, fk/2);
		if(fk & 1)  
			printf("%d\n", fk/2);
		else printf("%d\n", fk/2-1);
	} 
}
