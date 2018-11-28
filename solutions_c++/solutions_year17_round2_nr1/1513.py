#include<cstdio>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	int D, N;
	scanf(" %d %d ", &D, &N);
	int k, s;
	double time = -1.0;
	while(N > 0){
	    scanf(" %d %d ", &k, &s);
	    if((double)(D-k)/s > time) time = (double)(D-k)/s;
	    --N;
	}
	printf("Case #%d: %lf\n", t, D/time);
    }
    return 0;
}
