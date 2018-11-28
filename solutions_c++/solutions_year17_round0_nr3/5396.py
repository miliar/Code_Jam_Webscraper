#include <stdio.h>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>

#define endl "\n"

using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

pair<ll,ll> process(ll n, ll k){
	priority_queue< vector<ll> , vector< vector<ll> >, std::greater< vector<ll> > > pq;
	vector<ll> v;
	v.push_back(-n);
	v.push_back(1);
	v.push_back(n);
	pq.push(v);

	ll y, z;

	for(int i = 0; i < k; i++){
		vector<ll> t = pq.top();
		pq.pop();

		ll mid = -t[0];
		if(mid % 2 == 1) mid++;
		mid /= 2;
		mid = t[1] - 1 + mid;

		
		vector<ll> a;
		a.push_back(-mid + t[1]);
		a.push_back(t[1]);
		a.push_back(mid - 1);
		pq.push(a);

		//cout << "A: " << -a[0] << " " << a[1] << " " << a[2] << endl;

		vector<ll> b;
		b.push_back(-t[2] + mid);
		b.push_back(mid + 1);
		b.push_back(t[2]);
		pq.push(b);

		//cout << "B: " << -b[0] << " " << b[1] << " " << b[2] << endl;

		y = max(-a[0],-b[0]);
		z = min(-a[0],-b[0]);

	}

	return pair<ll,ll>(y,z);
}

int main(){
	ios::sync_with_stdio(0);

	int T;
	long long k, n;
	string str;
	cin >> T;
	for(int i = 1; i <= T; i++){
		cout << "Case #" << i << ": ";

		cin >> n >> k;
		
		pair<ll,ll> p = process(n, k);

		cout << p.first << " " << p.second;

		cout << endl;

	}

	
}
