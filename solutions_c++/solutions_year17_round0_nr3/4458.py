#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
const int MaxN = 1e6;
using namespace std;
priority_queue<int>que;
int T , a , b;
int main()
{
	freopen("C-small-2-attempt0.in" , "r" , stdin);
	freopen("C-small-2-attempt0.out" , "w" , stdout);
	scanf("%d" , &T);
	int cas = 0;
	while(T--){
		while(que.size()) que.pop();
		scanf("%d%d" , &a , &b);
		que.push(a);
		b--;
		while(b--){
			int t_x = que.top() / 2;
			int t_y = que.top() - t_x - 1;
			que.pop();
			que.push(t_x);
			que.push(t_y);
		}
		int ans_a = que.top() / 2;
		int ans_b = que.top() - ans_a - 1;
		printf("Case #%d: " , ++cas);
		printf("%d %d\n" , ans_a , ans_b);
	}
}
