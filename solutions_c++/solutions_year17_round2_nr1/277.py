#include <bits/stdc++.h>
using namespace std;

int T, D, N;

int main()
{
	for (scanf("%d", &T);T--;){
		scanf("%d%d", &D, &N);
		double t = 0;
		for (int i=1;i<=N;i++){
			int p, v; scanf("%d%d", &p, &v);
			t = max(t, (double)(D-p)/v);
		}
		static int ts = 0;
		printf("Case #%d: %.9f\n", ++ts, D/t);
	}
}