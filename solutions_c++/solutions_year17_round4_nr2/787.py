#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair<int , int> P2;
typedef pair<pair<int , int> , int> P3;
typedef pair<pair<int , int> , pair<int , int> > P4;
#define PB(a) push_back(a)
#define MP(a , b) make_pair((a) , (b))
#define M3P(a , b , c) make_pair(make_pair((a) , (b)) , (c))
#define M4P(a , b , c , d) make_pair(make_pair((a) , (b)) , make_pair((c) , (d)))
#define repp(i,a,b) for(int i = (int)(a) ; i < (int)(b) ; ++i)
#define repm(i,a,b) for(int i = (int)(a) ; i > (int)(b) ; --i)

int T;
int N,C,M;
bool r[1010][1010]; //car guest
int p[1010]; //seat
vector<P2> V;
vector<int> G[1010];
int d[1010];

void dft(){
	V.clear();
	fill(d,d+1010,0);
	fill(p,p+1010,0);
	repp(i,0,1010){
		fill(r[i],r[i]+1010,0);
		G[i].clear();
	}
}

int main(){
	scanf("%d" , &T);
	repp(tt,0,T){
		printf("Case #%d: " , tt+1);
		scanf("%d%d%d" , &N , &C , &M);
		dft();
		repp(i,0,M){
			int p,b;
			scanf("%d%d" , &p , &b);
			V.PB(MP(p,b));
			G[b].PB(p);
		}
		int ansr = 0 , ansp = 0;
		sort(V.begin(),V.end());
		for(auto u : V){
			repp(i,0,M){
				if(r[i][u.second]||d[i]>=u.first) continue;
				ansr = max(ansr,i+1);
				r[i][u.second] = 1;
				++d[i];
				break;
			}
		}
		repp(i,1,C+1){
			for(auto z : G[i]){
				if(p[z] < ansr) ++p[z];
				else ++ansp;
			}
		}
		printf("%d %d\n" , ansr , ansp);
	}
	return 0;
}
