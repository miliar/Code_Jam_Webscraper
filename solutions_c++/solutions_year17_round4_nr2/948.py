#include<bits/stdc++.h>
using namespace std;

int tick[1005];
int Count[1005][1005];

priority_queue<int>pq;

int main()
{
	int T,it,i,N,C,M,j,k;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for(it=1; it<=T; it++){
		scanf("%d", &N);
		scanf("%d%d", &C, &M);

		for(i=0; i<=N; i++){
			for(j=0; j<=C; j++)
				Count[i][j] = 0;
		}

		int cust, tick;
		for(i=0; i<M; i++){
			scanf("%d%d", &tick, &cust);
			Count[tick][cust]++;
		}

		while(!pq.empty())  pq.pop();

		vector<int>tmp;

		int cnt = 0;
		for(i=1; i<=C; i++)
			cnt += Count[1][i];

		for(i=1; i<=C; i++){
			int t=0;
			for(j=1; j<=N; j++)
				t += Count[j][i];
			cnt = max(cnt, t);
		}

		for(i=0; i<cnt; i++)
			pq.push(0);

		for(i=1; i<=N; i++){

			for(j=1; j<=C; j++){
				if(Count[i][j] == 0)  continue;
				while(Count[i][j] > pq.size())
					pq.push(0);
				tmp.clear();
				for(k=0; k<Count[i][j]; k++){
					tmp.push_back(pq.top());
					pq.pop();
				}
				for(k=0; k<tmp.size(); k++)
					pq.push(pq.top()-1);
			}
		}

		int ride = pq.size();
		while(!pq.empty())  pq.pop();

		for(i=0; i<ride; i++)  pq.push(0);

		int promo = 0;
		for(i=1; i<=N; i++){

			int tot = 0;
			for(j=1; j<=C; j++){
				tot += Count[i][j];
			}

			if(tot > ride){
				promo += (tot-ride);
			}
		}

		printf("Case #%d: %d %d\n", it, ride, promo);

	}
	return 0;
}