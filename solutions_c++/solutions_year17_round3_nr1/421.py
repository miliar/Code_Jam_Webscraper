#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
typedef pair<LL , LL> P2;
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
int K,N;
P2 P[1010];
priority_queue<LL,vector<LL>,greater<LL> > Q;
const double PI = 3.141592653536;

int main(){
	scanf("%d" , &T);
	repp(tt,0,T){
		printf("Case #%d: " , tt+1);
		scanf("%d%d" , &N , &K);
		fill(P,P+1010,MP(0,0));
		while(!Q.empty()) Q.pop();
		repp(i,0,N){
			int r,h;
			scanf("%d%d" , &r , &h);
			P[i] = MP(r,h);
		}
			sort(P,P+N,[&](const P2 a , const P2 b){
				return a.first == b.first ? a.second < b.second : a.first < b.first;
			});
		LL ans = 0 , z = 0;
		repp(i,0,K){
			Q.push(P[i].second*P[i].first);
			z += P[i].second*P[i].first;
		}
		ans = max(ans , z * 2 + (LL)P[K-1].first * P[K-1].first);
		repp(i,K,N){
			z -= Q.top();
			Q.pop();
			z += P[i].second * P[i].first;
			ans = max(ans , z * 2 + (LL)P[i].first * P[i].first);
			Q.push(P[i].second*P[i].first);
		}
		printf("%.9f\n" , PI * ans);
	}
	return 0;
}
