#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<queue>
using namespace std;
typedef long long LL;
int T;
priority_queue<LL> q; //优先队列
LL n, k;
int main(){
	freopen("C-small-2-attempt0.in.txt", "r", stdin);
	freopen("C-small-2-attempt0.out", "w", stdout);
	scanf("%d", &T);
	int Case = 0;
	while(T--){
		scanf("%lld %lld", &n, &k);
		LL cnt = 1;
		LL a, b;
		q.push(n);
		for(int i = 1; i <= k; i++){
			LL temp = q.top();
		//	printf("%lld ", temp);
			q.pop();
			a = (temp - 1) / 2;
			b = temp - 1 - a;
			if(i == k){
				printf("Case #%d: ", ++Case);
				printf("%lld %lld\n", max(a, b), min(a, b));
				break;
			}
			q.push(a);
			q.push(b);
		}
		while(!q.empty()) q.pop();
	}
	return 0;
}
		


