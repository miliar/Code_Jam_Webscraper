#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define pb push_back
#define INF 1000000000
#define mp make_pair
#define MOD 1000000007
#define F first;
#define S second;


int main() {
	
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int xyz = 1; xyz <= t; xyz++){
	    ll n,k,x,el;
	    cin >> n >> k;
	    priority_queue<ll> pq;
	    pq.push(n);
	    for (int i = 0; i < k-1; i++){
	        x = pq.top();
	        pq.pop();
	        pq.push(x/2);
	        pq.push((x-1)/2);
	    }
	    x = pq.top();
	    el = (x+1)/2;
	    cout << "Case #" << xyz << ": " << x-el << " " << el-1 << "\n";
	}
}
