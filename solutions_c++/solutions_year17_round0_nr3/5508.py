#include<stdio.h>
#include<queue>
#include<vector>
using namespace std;

struct point {
	int x, y;
};
point P[4000+3]; //
int Pcnt;


int main(void) {
	int T;
	int N, K;
	int i,j;
	int cost, index;
	int mid;
	int left, right;
	int a, b;

	priority_queue<pair<int,int>> pq;
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; i++) 
	{
		scanf("%d%d", &N, &K);
		while (!pq.empty()) pq.pop();
		pq.push(make_pair(N,0));
		P[0].x = 1; P[0].y = N;
		Pcnt = 0;//0~Pcnt���� ��

		for (j = 1; j < K; j++)
		{
			cost = pq.top().first;
			index = pq.top().second;
			left = P[index].x; right = P[index].y;
			mid = (left+right) / 2;
			pq.pop();
			//printf("*���� ���� �ִ� ���̴�%d\n", cost);
			
			//����
			Pcnt++;
			P[Pcnt].x = left; P[Pcnt].y = mid - 1;
	//		printf("���� ���̴� %d\n", (mid - left));
			pq.push(make_pair((mid-left),Pcnt));
			//������
			Pcnt++;
			P[Pcnt].x = mid + 1; P[Pcnt].y = right;
	//		printf("���� ���̴� %d\n", (right - mid));
			pq.push(make_pair((right - mid), Pcnt));

		}
		//K��°
		cost = pq.top().first;
	//	printf("*���� ���� �ִ� ���̴�%d\n", cost);
		index = pq.top().second;
		left = P[index].x; right = P[index].y;
		mid = (left + right) / 2;
		a = mid - left; b = right - mid;
		if (a > b) printf("Case #%d: %d %d\n",i,a,b);
		else printf("Case #%d: %d %d\n", i, b, a);
	}
}