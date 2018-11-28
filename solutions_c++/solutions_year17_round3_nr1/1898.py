#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>

#define MAX(a, b)	((a) > (b) ? (a) : (b))
#define MIN(a, b)	((a) < (b) ? (a) : (b))
#define ABS(a)		((a) < (0) ? (-(a)) : (a))

# define mpi		3.14159265358979323846

void setIO(const char * in = NULL, const char * out = NULL);


struct QQ{
	long double r, h;
};


bool cmp(QQ a, QQ b){
	if(a.r == b.r)
		return a.h < b.h;
	
	return a.r < b.r;
}

QQ A[1111];
long double dp[1111][1111];
long double ar[1111], suf[1111];


int main(){
	
	setIO("A-large.in", "file.out");
	
	int T; scanf("%d", &T);
	
	for(int c_s = 1; c_s <= T; ++c_s){
		
		int N, K;	scanf("%d %d", &N, &K);
		
		for(int i = 1; i <= N; ++i){
			scanf("%Lf %Lf", &A[i].r, &A[i].h);
			
			ar[i] = mpi * A[i].r * A[i].r;
			suf[i] = ar[i] + 2.0 * mpi * A[i].r * A[i].h;
		}
		
		
		std::sort(A + 1, A + N + 1, cmp);
		
		
		for(int i = 1; i <= N; ++i){
			ar[i] = mpi * A[i].r * A[i].r;
			suf[i] = ar[i] + 2.0 * mpi * A[i].r * A[i].h;
		}
		
		
		for(int i = 1; i <= N; ++i)
			dp[1][i] = suf[i];
		
		for(int i = 2; i <= K; ++i){
			
			for(int j = i; j <= N; ++j){
				
				long double v = 0;
				
				for(int k = i - 1; k < j; ++k){
					v = MAX(v, dp[i - 1][k] + suf[j] - ar[k]);
				}
				
				dp[i][j] = v;
			}
		}
		
		long double ans = 0;
		
		for(int i = K; i <= N; ++i){
			ans = MAX(ans, dp[K][i]);
		}
		
		printf("Case #%d: %.10Lf\n", c_s, ans);
		
	}
	
return 0;	
}

void setIO(const char * in, const char * out){
	if(in != NULL)	freopen(in, "r", stdin);
	if(out != NULL)	freopen(out, "w", stdout);
}
