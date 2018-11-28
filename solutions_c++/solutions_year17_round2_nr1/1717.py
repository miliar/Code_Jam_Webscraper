#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int T;
	cin >> T;
	int index = 0;

	while (index++ < T){
		int D, N;
		int K[1024], S[1024];
		scanf("%d %d", &D, &N);
		
		double maxT = 0;
		for(int i = 0; i < N; i ++)
		{
			scanf("%d %d", &K[i], &S[i]);
			maxT = max((double)(D-K[i])/S[i], maxT);
		}
		
		double ans = D/maxT;
		
		printf ("Case #%d: %lf\n", index, ans);
	}
	return 0;
}
