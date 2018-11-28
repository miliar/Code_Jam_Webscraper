#include <bits/stdc++.h>
using namespace std;

#define all(v) (v).begin(), (v).end()

int T;
int N, R, O, Y, G, B, V;
char A[1005];

int main()
{
	for (scanf("%d", &T);T--;){
		static int ts = 0;
		printf("Case #%d: ", ++ts);
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		int M = N >> 1;
		vector <pair<int, char>> arr = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
		sort(all(arr), greater<pair<int, char>>());
		if (arr[0].first > M){ puts("IMPOSSIBLE"); continue; }
		for (int i=1;i<=N;i+=2){
			for (int j=0;j<3;j++) if (arr[j].first > 0){
				arr[j].first--;
				A[i] = arr[j].second;
				break;
			}
		}
		for (int i=2;i<=N;i+=2){
			for (int j=0;j<3;j++) if (arr[j].first > 0){
				arr[j].first--;
				A[i] = arr[j].second;
				break;
			}
		}
		A[N+1] = 0;
		puts(A+1);
	}
}