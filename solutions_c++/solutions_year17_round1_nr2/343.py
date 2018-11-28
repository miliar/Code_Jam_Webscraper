#include<bits/stdc++.h>
using namespace std;
int n, p, re[100000], q[2000][2000], ll[2000][2000], rr[2000][2000];
vector<int> vec;
priority_queue<int> pq[10000];
int main(){
	freopen("B_large.in", "r", stdin);
	freopen("B_large.out", "w", stdout);
	int TT;
	cin >> TT;
	for(int ii = 1; ii <= TT; ii++){
		scanf("%d%d\n",&n,&p);
		for(int i = 1; i <= n; i++)
			while (!pq[i].empty())
				pq[i].pop();
		for(int i = 1; i <= n; i++)
			scanf("%d", &re[i]);
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= p; j++)
				scanf("%d", &q[j][i]);
		for(int i = 1; i <= p; i++){
			for(int j = 1; j <= n; j++){
				ll[i][j] = rr[i][j] = -1;
				int r = (10 * q[i][j]) / (9 * re[j]);
				int l = (10 * q[i][j] + 11 * re[j] - 1) / (11 * re[j]);
				l = max(l, 1);
				if(l > r) continue;
				ll[i][j] = l;
				rr[i][j] = r;
				vec.push_back(l);
				vec.push_back(r);
			}
		}
		int ans = 0;
		sort(vec.begin(), vec.end());
		vec.erase(unique(vec.begin(), vec.end()), vec.end());
		for(int zi = 0; zi < (int)vec.size(); zi++){
			int tmp = vec[zi];
			for(int i = 1; i <= p; i++)
				for(int j = 1; j <= n; j++)
					if(ll[i][j] == tmp){
						pq[j].push(-rr[i][j]);
						//cout<<"push  "<<-rr[i][j]<<endl;
					}
			while(1){
				bool flag = true;
				for(int i = 1; i <= n; i++)
					if(pq[i].empty())
						flag = false;
				if(!flag) break;
				ans++;
				for(int i = 1; i <= n; i++){
					//cout<<"pop1  "<<pq[i].top()<<endl;
					pq[i].pop();
				}
			}
			for(int i = 1; i <= n; i++){
				while(!pq[i].empty() && pq[i].top() == -tmp){
					//cout<<"pop0  "<<pq[i].top()<<endl;
					pq[i].pop();
				}
			}
		}
		printf("Case #%d: %d\n", ii, ans);
	}
}
