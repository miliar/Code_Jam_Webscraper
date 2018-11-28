#include <queue>
#include <stdio.h>

void bathroom(int N, int K, int* ma, int* mi)
{
	std::priority_queue<int> q;
	q.push(N);
	int l=0,r=0;
	for (int i=0;i<K;i++) {
		int x = q.top();
		x--;
		l = x>>1;
		r = l + (x&0x1);
		q.pop();
		q.push(r);
		q.push(l);
	}
	*ma = r;
	*mi = l;
}


int main()
{
	int T;
	int N,K;
	int ma, mi;
	scanf("%d", &T);
	for (int i=0;i<T;i++) {
		scanf("%d %d", &N, &K);

		bathroom(N,K, &ma, &mi);

		printf("Case #%d: %d %d\n", i+1,ma, mi);
	}
}
