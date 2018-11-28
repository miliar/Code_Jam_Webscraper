#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
    double pi = 3.1415926535898;
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	int N, K;
	scanf(" %d %d ", &N, &K);
	int radius[N];
	int height[N];
	double area[N];
	double cylinder[N];
	for(int i=0; i<N; ++i){
	    scanf(" %d %d ", &radius[i], &height[i]);
	    cylinder[i] = pi*radius[i]*2.0*height[i];
	    area[i] = pi*radius[i]*radius[i];
	}
	double res = 0.0;
	double tmp;
	double cand[N];
	int cnt;
	for(int i=0; i<N; ++i){
	    tmp = cylinder[i]+area[i];
	    for(int j=0; j<N; ++j) cand[j] = 0.0;
	    cnt = 0;
	    for(int j=0; j<N; ++j){
		if(j == i) continue;
		if(area[j] <= area[i]){
		    cand[j] = cylinder[j];
		    ++cnt;
		}
	    }
	    if(cnt < K-1) continue;
	    sort(cand, cand+N);
	    for(int j=0; j<K-1; ++j){
		tmp += cand[N-1-j];
	    }
	    res = (tmp > res ? tmp : res);
	}
	printf("Case #%d: %lf\n", t, res);
    }
    return 0;
}
