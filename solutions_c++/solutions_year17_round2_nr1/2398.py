#include <bits/stdc++.h>

#define ff first
#define ss second
#define mp make_pair

using namespace std;

int main(){
		int T;

		scanf("%d", &T);

		for(int t = 1; t <= T; t++){
				int n,d;
				scanf("%d%d", &d, &n);

				pair<int,int> v;
				double tempo = 0;
				for(int i = 0; i < n; i++){
						scanf("%d%d", &v.ff, &v.ss);
						tempo = max(tempo,((double)d-v.ff)/v.ss);
				}

				printf("Case #%d: %.15lf\n", t, d/tempo);

		}

	return 0;
}
