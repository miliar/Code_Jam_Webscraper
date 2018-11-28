#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF (1111111)
#define maxn 511

typedef long long ll;
typedef long double ld;

priority_queue<int> pq;
ld p[maxn];

ld solve(){
	int n, k;
	scanf("%d%d", &n, &k);
	int a, b;
	scanf("%d.%d", &a, &b);
	ld dod = 10000 * a + b; 

	for(int i = 0; i < n; i++){
		int a, b;
		scanf("%d.%d", &a, &b);
		p[i] = 10000 * a + b; 
		pq.push(-p[i]);
	}

	for(int i = 0; i < dod; i++){
		int x = -pq.top();
		pq.pop();

		if(x < 10000)
			x++;
		pq.push(-x);
	}

	ld ans = 1.0;

	while(!pq.empty()){
		ans *= (1.0 * -pq.top() / 10000.0);
		pq.pop();
	}

	return ans;
}



int main(){
	ll t;
	cin >> t;
	for(ll ll = 1; ll <= t; ll++){
		cout << fixed << setprecision(10) << "Case #" << ll << ": " << solve() << endl;
	}
	return 0;
}