#include <cstdio>
#include <set>
#include <queue>
#include <iostream>

using namespace std;

const int N = 1100000;

int nc = 0;

typedef long long ll;

int calc(ll x,ll k){
	priority_queue<int>Q;
	while(!Q.empty()) Q.pop();
	Q.push(x);
	int y;
	while(k--){
		int u = Q.top();
		Q.pop();
		x = (u - 1) / 2;
		y = u / 2;
		Q.push(x);
		Q.push(y);
	}
	cout << "Case #" << ++nc << ": ";
	cout << y << " " << x << endl;
}

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	while(T--){
		ll x,y;
		cin >> x >> y;
		calc(x,y);
	}
}
