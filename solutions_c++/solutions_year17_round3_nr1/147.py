#include<stdio.h>
#include<algorithm>

using namespace std;

int N, M;
int T;
long double R[10000], H[10000], D[10000];
long double Ret;
long double Curr;
long double Pi = 3.1415926535897932384626433832795;
long double EPS = 1e-8;

int main(void)
{
	int l0;
	int l1, l2, l3, l4;
	int cnt;

	scanf("%d", &T);
	for(l0 = 1; l0 <= T; l0++)
	{
		scanf("%d %d", &N, &M);
		for(l1 = 0; l1 < N; l1++)
		{
			scanf("%Lf %Lf", &R[l1], &H[l1]);
			D[l1] = 2 * Pi * R[l1] * H[l1];
		}

		for(l1 = 0; l1 < N; l1++)
		{
			for(l2 = l1+1; l2 < N; l2++)
			{
				if(D[l1] < D[l2])
				{
					swap(D[l1], D[l2]);
					swap(R[l1], R[l2]);
					swap(H[l1], H[l2]);
				}
			}
		}

		Ret = -1;
		for(l1 = 0; l1 < N; l1++)
		{
			Curr = D[l1] + Pi * R[l1] * R[l1];

			cnt = 1;
			for(l2 = 0; l2 < N; l2++)
			{
				if(cnt == M) break;
				if(l1 == l2) continue;
				if(R[l2] > R[l1]+1) continue;
				cnt++;
				Curr += D[l2];
			}
			if(cnt == M && Curr > Ret) Ret = Curr;
		}

		printf("Case #%d: %.20Lf\n", l0, Ret);
	}

	return 0;
}

