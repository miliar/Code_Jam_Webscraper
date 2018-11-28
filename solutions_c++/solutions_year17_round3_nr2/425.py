#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
typedef pair<int , int> P2;
typedef pair<pair<int , int> , int> P3;
typedef pair<pair<int , int> , pair<int , int> > P4;
#define Fst first
#define Snd second
#define PB(a) push_back(a)
#define MP(a , b) make_pair((a) , (b))
#define M3P(a , b , c) make_pair(make_pair((a) , (b)) , (c))
#define M4P(a , b , c , d) make_pair(make_pair((a) , (b)) , make_pair((c) , (d)))
#define repp(i,a,b) for(int i = (int)(a) ; i < (int)(b) ; ++i)
#define repm(i,a,b) for(int i = (int)(a) ; i > (int)(b) ; --i)

int T;
int A,B;
bool c[1500] , d[1500];
int dp[2][2][1500][723];
const int INF = 1e9 + 7;
const int Day = 1440;
const int Work = 720;

void def(){
	fill(c,c+1500,0);
	fill(d,d+1500,0);
	repp(i,0,1500){
		repp(j,0,4){
			fill(dp[j%2][j/2][i],dp[j%2][j/2][i]+723,INF);
		}
	}
}

int main(){
	scanf("%d" , &T);
	repp(tt,0,T){
		printf("Case #%d: " , tt+1);
		scanf("%d%d" , &A , &B);
		def();
		repp(i,0,A){
			int x,y;
			scanf("%d%d" , &x , &y);
			repp(j,x,y) c[j] = 1;
		}
		repp(i,0,B){
			int x,y;
			scanf("%d%d" , &x , &y);
			repp(j,x,y) d[j] = 1;
		}
		dp[0][0][0][0] = 0;
		dp[0][1][0][0] = 1;
		dp[1][1][0][0] = 0;
		dp[1][0][0][0] = 1;
		repp(u,0,Day){
			repp(v,0,Work+1){
				repp(i,0,2){
					if(!c[u]&&v<Work){
						dp[i][0][u+1][v+1] = min(dp[i][0][u+1][v+1],dp[i][0][u][v]);
						dp[i][0][u+1][v+1] = min(dp[i][0][u+1][v+1],dp[i][1][u][v]+1);
					}
					if(!d[u]&&u-v<Work){
						dp[i][1][u+1][v] = min(dp[i][1][u+1][v],dp[i][0][u][v]+1);
						dp[i][1][u+1][v] = min(dp[i][1][u+1][v],dp[i][1][u][v]);
					}
					//printf("%d %d %d %d %d\n" , u+1 , v , i , dp[i][0][u+1][v] , dp[i][1][u+1][v]);
				}
			}
		}
		printf("%d\n" , min(min(dp[0][0][Day][Work],dp[0][1][Day][Work]+1),min(dp[1][1][Day][Work],dp[1][0][Day][Work]+1)));
	}
	return 0;
}
