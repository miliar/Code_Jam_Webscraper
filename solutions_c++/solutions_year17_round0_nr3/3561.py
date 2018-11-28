#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int t, n,k,num;
priority_queue<int>  heap;

int main()
{
	scanf("%d", &t);
	for (int test = 1; test <= t; test++){
		printf("Case #%d: ", test);
		scanf("%d %d", &n, &k);
		if (k == 1){
			if (n & 1)printf("%d %d\n", n / 2, n / 2);
			else printf("%d %d\n", n / 2, (n - 1) / 2);
		}
		else{
			k--;
			if (n & 1){
				heap.push((n / 2));
				heap.push((n / 2));
			}
			else {
				heap.push((n / 2));
				if (n !=2)heap.push(((n-1)/ 2));
			}
			for (;;){
				num = heap.top();
				k--;
				if (k == 0)break;
				heap.pop();
				if (num & 1){
					if (num != 1){
						heap.push((num / 2));
						heap.push((num / 2));
					}
				}
				else{
					heap.push((num / 2));
					if (num != 2)heap.push(((num - 1) / 2));
				}
			}
			if (num & 1)printf("%d %d\n", num / 2, num / 2);
			else printf("%d %d\n", num / 2, (num - 1) / 2);
		}
		while (!heap.empty())heap.pop();

	}
	return 0;
}