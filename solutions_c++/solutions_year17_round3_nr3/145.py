#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

vector< long double > A;
long double U;
int T, N, M;
long double EPS = 1e-12;
long double Curr;
long double Ret;

int main(void)
{
	int l0, l1, l2;

	cin >> T;
	for(l0 = 1; l0 <= T; l0++)
	{
		cin >> N >> M >> U;
		A.resize(N);
		for(l1 = 0; l1 < N; l1++) cin >> A[l1];
		sort(A.begin(), A.end());

		Ret = 1;
		for(l1 = 0; l1 < N; l1++) Ret *= A[l1];
		
		for(l1 = 0; l1 < N; l1++)
		{
			long double at_least = 0;
			for(l2 = 0; l2 <= l1; l2++)
			{
				at_least += (A[l1] - A[l2]);
			}
			if(at_least > U) continue;

			long double target = A[l1] + (U - at_least) / (long double)(l1+1);
			if(target > 1) target = 1;

			Curr = 1;
			for(l2 = 0; l2 <= l1; l2++) Curr *= target;
			for(l2 = l1+1; l2 < N; l2++) Curr *= A[l2];
			if(Curr > Ret) Ret = Curr;
		}

		printf("Case #%d: %.20Lf\n", l0, Ret);
	}
	return 0;
}
