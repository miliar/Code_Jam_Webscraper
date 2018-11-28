#include <stdio.h>
#include <math.h>
long long int mymin(long long int a, long long int b) {
	return a<=b? a:b;
}

long long int* solve(long long int N, long long int K) {
	static long long int ans[2];
	if (K==0) return ans;
	if (K==1) {
		if (N%2==0) {
			ans[0]=N/2;
			ans[1]=N/2-1;
		}
		else {
			ans[0]=ans[1]=N/2;
		}
		return ans;
	}
	int cnt=log2(K);
	long long int large, small;
	long long int large_cnt, small_cnt;

	if (N%2==0) {
		large=N/2;
		small=large-1;
		large_cnt=1;
		small_cnt=1;
	}
	else {
		large=-1;
		small=N/2;
		large_cnt=0;
		small_cnt=2;
	}

	for (int i=0; i<cnt; i++) {
		long long int tmp_large_cnt=large_cnt;
		long long int tmp_small_cnt=small_cnt;
		long long int tmp_large=large;
		long long int tmp_small=small;
		large_cnt=0;
		small_cnt=0;

		if (tmp_large_cnt==0) {
			if (tmp_small%2==0) {
				large=tmp_small/2;
				small=tmp_small/2-1;
				large_cnt+=tmp_small_cnt;
				small_cnt+=tmp_small_cnt;
			}
			else {
				small=tmp_small/2;
				small_cnt+=tmp_small_cnt*2;
			}
		}
		else {
			if (tmp_large%2==0) {
				large=tmp_large/2;
				small=tmp_large/2-1;
				large_cnt+=tmp_large_cnt;
				small_cnt+=tmp_large_cnt+tmp_small_cnt*2;
			}
			else {
				large=tmp_large/2;
				small=tmp_large/2-1;
				large_cnt+=tmp_large_cnt*2+tmp_small_cnt;
				small_cnt+=tmp_small_cnt;
			}
		}
	
	}

	if (large==0) {
		ans[0]=ans[1]=0;
		return ans;
	}


	long long int cur=1;
	for (int i=0; i<cnt; i++) cur<<=1; 
	cur--;

	//printf("N=%lld K=%lld k-cur=%lld\n", N, K, K-cur);
	
	long long int num_large, num_pair, num_small;
	num_pair=mymin(large_cnt, small_cnt);
	num_large=(large_cnt-num_pair)/2;
	num_small=(small_cnt-num_pair)/2;

	if (K-cur <= num_large) {
		ans[0]=ans[1]=large;
	}
	else if (K-cur-num_large <= num_pair) {
		ans[0]=large;
		ans[1]=small;
	}
	else {
		ans[0]=ans[1]=small;
	}

	return ans;
}

int main() {

	int T;
	long long int N, K;
	scanf("%d", &T);

	for (int i=0; i<T; i++) {
		scanf("%lld%lld", &N, &K);
		long long int *ans = solve(N, K);
		printf("Case #%ld: %lld %lld\n", i+1, ans[0], ans[1]);
	}
	return 0;
}
