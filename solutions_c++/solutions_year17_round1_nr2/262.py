#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

int a(long long p, long long q)
{
	return (11 * p + 10 * q - 1) / (11 * p);
}

int b(long long p, long long q)
{
	return (10 * q) / (9 * p);
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		int N,M; scanf ("%d %d",&N,&M);
		int P[55];
		for (int i=0;i<N;i++) scanf ("%d",&P[i]);
		vector<pair<int, int> > u[55];
		for (int i=0;i<N;i++){
			for (int j=0;j<M;j++){
				int x; scanf ("%d",&x);

				int s = a(P[i],x), e = b(P[i],x);
				if (s <= e){
					u[i].push_back({s,e});
				}
			}
			sort(u[i].begin(),u[i].end());
		}

		int p[55] = {0,}, ans = 0;
		while (1){
			int mn = 0x7fffffff, pos = -1, a = 0x80000000, b = 0x7fffffff;
			for (int i=0;i<N;i++){
				if (p[i] == u[i].size()){
					mn = -1;
					break;
				}
				if (mn > u[i][p[i]].first){
					mn = u[i][p[i]].first;
					pos = i;
				}
				a = max(a,u[i][p[i]].first);
				b = min(b,u[i][p[i]].second);
			}
			if (mn < 0) break;
			if (a <= b){
				for (int i=0;i<N;i++) p[i]++;
				ans++;
			}
			else p[pos]++;
		}

		printf ("Case #%d: %d\n",Case,ans);
	}

	return 0;
}