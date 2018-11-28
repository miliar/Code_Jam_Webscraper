#include<cstdio>
using namespace std;

int main(){
    int T;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	int N, Q;
	scanf(" %d %d ", &N, &Q);
	int HS[N][2]; // E, S
	for(int i=0; i<N; ++i){
	    scanf(" %d %d ", &HS[i][0], &HS[i][1]);
	}
	int D[N][N];
	for(int i=0; i<N; ++i){
	    for(int j=0; j<N; ++j){
		scanf(" %d ", &D[i][j]);
	    }
	}
	int M[Q][2]; // U, V
	for(int i=0; i<Q; ++i){
	    scanf(" %d %d ", &M[i][0], &M[i][1]);
	}
	
	double D2[N];
	D2[0] = 0.0;
	for(int i=1; i<N; ++i) D2[i] = D2[i-1] + D[i-1][i];
	double min[N];
	min[0] = 0.0;
	min[1] = (double)D2[1] / HS[0][1];
	for(int i=2; i<N; ++i){
	    min[i] = -1.0;
	    for(int j=0; j<i; ++j){
		if(D2[i]-D2[j] <= HS[j][0]){
		    double tmp = (double)(D2[i]-D2[j])/HS[j][1] + min[j];
		    min[i] = (min[i] == -1.0 || tmp < min[i] ? tmp : min[i]);
		}
	    }
	}
	printf("Case #%d: %lf\n", t, min[N-1]);
    }
    return 0;
}
