#include <bits/stdc++.h>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int N, K;

int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		cin >> N >> K;
		priority_queue<int> pq;
		pq.push(N);
		ii ans;
		for(int i = 0; i < K; i++){
			int x = pq.top()-1; pq.pop();
			int l = (int)ceil(x/2.0);
			int r = x/2;
			pq.push(l); pq.push(r);
			ans = {l,r};
		}
		printf("Case #%d: %d %d\n",caso,ans.F,ans.S);
	}
	return 0;
}
