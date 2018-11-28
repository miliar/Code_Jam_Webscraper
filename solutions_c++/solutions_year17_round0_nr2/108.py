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
LL N;
int d[22];

int main(){
	scanf("%d" , &T);
	repp(i,0,T){
		printf("Case #%d: " , i + 1);
		scanf("%lld" , &N);
		int x = 0;
		while(N > 0){
			d[x] = N % 10;
			++x;
			N /= 10;
		}
		repm(j,x-1,0){
			if(d[j] > d[j-1]){
				while(d[j] > d[j-1] && j < x){
					--d[j];
					++j;
				}
				--j;
				repp(k,0,j){
					d[k] = 9;
				}
				break;
			}
		}
		while(d[x-1] == 0) --x;
		repm(i,x-1,-1){
			printf("%d" , d[i]);
		}
		printf("\n");
	}
	return 0;
}
