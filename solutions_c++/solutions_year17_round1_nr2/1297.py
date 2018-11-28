#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	int N, P;
	scanf(" %d %d ", &N, &P);
	if(N == 1){
	    int R;
	    scanf(" %d ", &R);
	    int res = 0;
	    int Q;
	    for(int i=0; i<P; ++i){
		scanf(" %d ", &Q);
		int r = floor(Q / (R * 0.9));
		int l = ceil(Q / (R * 1.1));
		if(r == 0) continue;
		res += (l <= r ? 1 : 0);
	    }
	    printf("Case #%d: %d\n", t, res);
	}else{
	    int R1, R2;
	    scanf(" %d %d ", &R1, &R2);
	    int Q1[P];
	    int Q2[P];
	    for(int i=0; i<P; ++i){
		scanf(" %d ", &Q1[i]);
	    }
	    for(int i=0; i<P; ++i){
		scanf(" %d ", &Q2[i]);
	    }
	    sort(Q1, Q1+P);
	    sort(Q2, Q2+P);
	    int ind1 = 0;
	    int ind2 = 0;
	    int res = 0;
	    while(ind1 < P && ind2 < P){
		int r1 = floor(Q1[ind1] / (R1 * 0.9));
		int l1 = ceil(Q1[ind1] / (R1 * 1.1));
		if(r1 < l1 || r1 == 0){
		    ++ind1;
		    continue;
		}
		int r2 = floor(Q2[ind2] / (R2 * 0.9));
		int l2 = ceil(Q2[ind2] / (R2 * 1.1));
		if(r2 < l2 || r2 == 0){
		    ++ind2;
		    continue;
		}
		if(r1 < l2){
		    ++ind1;
		    continue;
		}
		if(r2 < l1){
		    ++ind2;
		    continue;
		}
		++res;
		++ind1;
		++ind2;
	    }
	    printf("Case #%d: %d\n", t, res);
	}
    }
    return 0;
}
