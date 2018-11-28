#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>
//#include <priority_queue>
#include <queue>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000
#define F first
#define S second
#define forn(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,b) for(int i = 0; i < (b); i++)

using namespace std;




int main(){
	int tcase;
	scanf("%d", &tcase);
	for(int tc = 1; tc <= tcase; tc++){
		int n,k;
		scanf("%d %d", &n, &k);
		priority_queue<int> pq;
		pq.push(n);
		int l,r;
		rep(i,k){
			int a = pq.top();
			pq.pop();
			r = a/2;
			l = a-1-r;
			pq.push(l);
			pq.push(r);
		}
		printf("Case #%d: %d %d\n", tc, r, l);
	}

	return 0;
}
