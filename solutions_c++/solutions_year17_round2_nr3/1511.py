#include <bits/stdc++.h>

using namespace std;

#define MAX 1LL<<62
#define MIN -2147483647
#define clear_arr(a) memset(a,0,sizeof(a))
#define pb push_back

typedef double ll;
typedef pair<double,double> ii;
typedef pair<string,string> ss;
typedef vector<ss> vss;
typedef pair<ll, ii> iii;
typedef vector<double> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<string> vs;
typedef vector<ii> vii;
typedef deque<ll> dqi;
typedef unordered_set<ll> usi;
typedef set<ll> si;
typedef unordered_set<ii> usii;
typedef set<ii> sii;
typedef unordered_map<ll,ll> umii;
typedef map<ll,ll> mii; 
typedef map<string,int> msi;
typedef map<int,string> mis;

double grid[105][105], path[105][105];
int n, queries;
ii horses[105];
vi times[105];
vi reach[105];

void reset_var(){
	for(int i=0;i<100;i++){
		for(int j=0;j<100;j++){
			if(i != j and grid[i][j] == -1)
				grid[i][j] == MAX;
			if(i == j and grid[i][j] == -1)
				grid[i][j] = 0;
			path[i][j] = i;
		}
	}
}

int main(){
	int cases;
	scanf("%d",&cases);
	double dist[105];

	for(int xl=1;xl<=cases;xl++){
		scanf("%d %d", &n, &queries);
		for(int i=0;i<105;i++){
			times[i].assign(105,MAX);
			reach[i].assign(103,0);
		}
		times[1].assign(105,0);
		times[0].assign(105,0);
		for(int i=1;i<=n;i++){
			scanf("%lf %lf", &horses[i].first, &horses[i].second);
			// printf("%lf %lf\n",horses[i].first, horses[i].second );
		}
		clear_arr(grid);
		for(int i=1;i<=n;i++){
			for(int j=1;j<=n;j++){
				scanf("%lf", &grid[i][j]);
			}
		}
		double distance = 0;
		double time_ = 0;
		clear_arr(dist);

		for(int i=1;i<=n;i++){
			dist[i] = grid[i-1][i];
		}
		for(int i=1;i<=n;i++){
			dist[i] = dist[i] + dist[i-1];
		}
		// for(int i=1;i<=n;i++)
		// 	printf("%.1lf  ",dist[i] );
		// printf("\n");

		int a,b;
		for(int i=0;i<queries;i++){
			scanf("%d %d", &a, &b);
		}
		for(int i=2;i<=n;i++){
			for(int j=1;j<i;j++){
				if(horses[j].first >= dist[i] - dist[j]){
					reach[i][j] = 1;
				}
			}
		}
		for(int i=2;i<=n;i++){
			for(int j=1;j<i;j++){
				if(horses[j].first >= dist[i] - dist[j] and times[j][0] < MAX){
					// if(xl == 84)
					// 	printf("dist[i] : %lf\tdist[j]: %lf\t horses[j].second = %lf\n",dist[i], dist[j], horses[j].second );
					times[i][0] = min(times[i][0],  times[j][0]+(dist[i]-dist[j])/horses[j].second);
				}
			}
			// if(xl == 84){
			// 	if(times[i][0] == MAX)
			// 		printf("flag\n");
			// 	printf("i: %d\ttime : %lf\n\n\n",i, times[i][0] );
			// }
		}
		// if(xl != 84)
		// 	continue;
			printf("Case #%d: ", xl);
			printf("%.6lf\n",times[n][0] );
	}
	return 0;
}


		// reset_var();
		// for(int k=1;k<=n;k++){
		// 	for(int i=1;i<=n;i++){
		// 		for(int j=1;j<=n;j++){
		// 			if(grid[i][j] > grid[i][k] + grid[k][j]){
						
		// 			}
		// 		}
		// 	}
		// }