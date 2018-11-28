#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

int n, k;
priority_queue<int> pq;

int main() {
	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		scanf("%d%d", &n, &k);

		pq.push(n);
		int ans1 = -1, ans2 = -1;
		for(int i=0; i<k; i++) {
			int x = pq.top(); pq.pop();
			ans1 = (x-1)/2, ans2 = x-1-(x-1)/2;
			pq.push((x-1)/2);
			pq.push(x-1-(x-1)/2);
		}

		printf("Case #%d: %d %d\n", kase, ans2, ans1);

		while(!pq.empty())	pq.pop();
	}
    
    return 0;
}
