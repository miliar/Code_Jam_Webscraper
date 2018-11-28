#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second

using namespace std;

int horse[1010][2];

int main(int argc, char* argv[]){
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		int N;
		double D;
		scanf("%lf%d", &D, &N);
		for(int i = 0; i < N; i++)
			scanf("%d%d", &horse[i][0], &horse[i][1]);
	
		double l, r;
		l = 0, r = 1e16;
		while(abs(l-r) > 1e-6){
			double m = l+((r-l)/(double)2.0);
			double diff = (r-l)/2.0;
			if(abs(l-(l+diff))<1e-6) break;
			bool flag = true;
			for(int i = 0; i < N; i++)
				if(D/m < (D-horse[i][0])/horse[i][1]){
					flag = false;
					break;
				}
			if(flag)
				l = m+1e-6;
			else
				r = m;
		}
		printf("%.8f\n", l);
	} 
    return 0;
}
