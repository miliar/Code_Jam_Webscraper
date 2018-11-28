#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#define pb push_back

using namespace std;

priority_queue<int> pq;

int main() {
	int n,t,k,num1,num2;
	scanf("%d",&t);
	for (int ctr=1;ctr<=t;ctr++) {
		scanf("%d %d",&n,&k);
		while (!pq.empty()) pq.pop();
		int acc = 1;
		if (n%2==0) {
			num1 = n/2;
			num2 = num1-1;
		}
		else {
			num1 = n/2;
			num2 = n/2;
		}
		pq.push(num1);
		pq.push(num2);
		
		printf("Case #%d: ",ctr);
		
		if (k==1) printf("%d %d\n",max(num1,num2),min(num1,num2));
		else {
			while (!pq.empty()) {
				int cur = pq.top();
				pq.pop();
				cur--;
				if (cur%2==0) {
					num1 = cur/2;
					num2 = cur/2;
				}
				else {
					num1 = cur/2;
					num2 = num1+1;
				}
				acc++;
				if (acc==k) {
					printf("%d %d\n",max(num1,num2),min(num1,num2));
					break;
				}
				pq.push(num1);
				pq.push(num2);
			}
		}
	}
	return 0;
}