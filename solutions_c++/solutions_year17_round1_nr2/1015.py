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

int T,N,P;
int R[55];
int Q[55][55];
int S[55];

int main(){
	scanf("%d" , &T);
	repp(tt,0,T){
		printf("Case #%d: " , tt+1);
		scanf("%d%d" , &N , &P);
		repp(i,0,N){
			scanf("%d" , R + i);
			S[i] = 0;
		}
		repp(i,0,N){
			repp(j,0,P){
				scanf("%d" , Q[i]+j);
			}
			sort(Q[i],Q[i]+P);
		}
		int ans = 0;
		repp(i,1,1000001){
			int b = 0;
			repp(j,0,N){
				int x = R[j] * i * 0.9 + 0.99;
				int y = R[j] * i * 1.1;
				while(S[j] < P && Q[j][S[j]] < x) ++S[j];
				if(S[j] >= P){
					b = -1;
					break;
				}
				if(Q[j][S[j]] > y){
					b = 1;
					break;
				}
			}
			if(b<0) break;
			if(b>0) continue;
			++ans;
			repp(j,0,N) ++S[j];
			--i;
		}
		printf("%d\n" , ans);
	}
	return 0;
}
