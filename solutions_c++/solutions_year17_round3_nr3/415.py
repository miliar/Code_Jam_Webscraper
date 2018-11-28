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
int N,K;
int U;
int P[55];
int z[10010];

int read(){
	char c[8];
	scanf(" %s" , c);
	return (c[0]-'0') * 10000 + (c[2]-'0') * 1000 + (c[3]-'0') * 100 + (c[4]-'0') * 10 + (c[5]-'0');
}

void dft(){
	fill(z,z+10010,0);
	fill(P,P+55,0);
}

int main(){
	scanf("%d" , &T);
	repp(tt,0,T){
		printf("Case #%d: " , tt+1);
		dft();
		scanf("%d%d" , &N , &K);
		int x1,x2;
		scanf("%d.%d" , &x1 , &x2);
		U = x1 * 10000 + x2;
		repp(i,0,N){
			P[i] = read();
			++z[P[i]];
		}
		int r = 0;
		repp(i,0,U){
			while(z[r]==0) ++r;
			--z[r];
			++z[r+1];
		}
		double ans = 1.0;
		repp(i,0,10010){
			repp(j,0,z[i]){
				ans *= i / 10000.0;
			}
		}
		printf("%.12f\n" , ans);
	}
	return 0;
}
