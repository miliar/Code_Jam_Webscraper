#include<bits/stdc++.h>
using namespace std;

int amount[55];
vector<int>A[55];
int N,P;

// 0 is valid, -1 is y is smaller, +1 is y is greater
int valid(int x, int y)//y is valid wrt x
{
	if(9*x > 10*y)  return -1;
	if(9*x <= 10*y && 10*y <= 11*x)  return 0;
	if(10*y > 11*x)  return 1;
}

int last[55];

int main()
{
	int T,it,kk;
	int i,j,k;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &T);

	for(it=1; it<=T; it++){

		scanf("%d%d", &N,&P);
		for(i=0; i<N; i++)  scanf("%d", &amount[i]);

		for(i=0; i<N; i++)  A[i].clear();
		for(i=0; i<N; i++){
			for(j=0; j<P; j++){
				scanf("%d", &kk);
				A[i].push_back(kk);
			}
			sort(A[i].begin(), A[i].end());
		}

		int ans = 0;

		for(i=0; i<N; i++)  last[i] = -1;

		for(i=0; i<P; i++){

			int nq = A[0][i]/amount[0];

			// if(valid(q*amount[0], A[0][i]) != 0){
			// 	q++;
			// 	if(valid(q*amount[0], A[0][i]) != 0) continue;
			// }

			int qq = nq;
			bool found = 0;
			while(valid(qq*amount[0], A[0][i]) != 1) qq--;

			for(int q = qq; q<=nq; q++){
				if(valid(q*amount[0], A[0][i]) != 0){
					continue;
				}

				int cnt = 0;
				for(j=1; j<N; j++){//other ingredients

					for(k=last[j]+1; k<P; k++){
						if(valid(q*amount[j], A[j][k]) == 0){
							cnt++;break;
						}
					}
				} 

				if(cnt < N-1){
					continue;
				}
				//printf("i:%d\n", i);
				ans++;
				found =1;


				for(j=1; j<N; j++){//other ingredients

					for(k=last[j]+1; k<P; k++){
						if(valid(q*amount[j], A[j][k]) == 0){
							last[j] = k; break;
						}
					}
				} 
				break;
			}

			if(found)  continue;
			int q = nq;

			while(valid(q*amount[0], A[0][i]) != -1){

				if(valid(q*amount[0], A[0][i]) != 0){
					q++;continue;
				}

				int cnt = 0;
				for(j=1; j<N; j++){//other ingredients

					for(k=last[j]+1; k<P; k++){
						if(valid(q*amount[j], A[j][k]) == 0){
							cnt++;break;
						}
					}
				} 

				if(cnt < N-1){
					q++;continue;
				}
				ans++;

				for(j=1; j<N; j++){//other ingredients

					for(k=last[j]+1; k<P; k++){
						if(valid(q*amount[j], A[j][k]) == 0){
							last[j] = k; break;
						}
					}
				} 
				break;
			}

		}

		printf("Case #%d: %d\n", it, ans);
	}
	return 0;
}