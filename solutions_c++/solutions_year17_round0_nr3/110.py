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
LL N,K;

int main(){
	scanf("%d" , &T);
	repp(t,0,T){
		printf("Case #%d: " , t + 1);
		scanf("%lld%lld" , &N , &K);
		LL a = N , c = 1 , d = 0 , p = 0;
		while(p < K){
			if(c + p >= K){
				p += c;
				printf("%lld %lld\n" , a / 2 , (a-1) / 2);
			} else if(c + d + p >= K){
				p += c + d;
				printf("%lld %lld\n" , (a-1) / 2 , (a-2) / 2);
			} else {
				p += c + d;
				if(a % 2 == 0){
					d = c + 2 * d;
				} else {
					c = c * 2 + d;
				}
				a /= 2;
			}
		}
	}
	return 0;
}
