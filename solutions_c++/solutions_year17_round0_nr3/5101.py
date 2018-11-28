#include <iostream>
#include <string>
#include <cmath>

typedef long long int ll;

using namespace std;

void testcase(int ncase, ll N, ll K){
	cout << "Case #" << ncase << ": ";
	ll ans = 0;
	int L = ceil(log2(N+1));
	int l = ceil(log2(K+1));

	if ( l == L ){
		cout << 0 << " " << 0 << endl;
		return;
	}

	ll n = (1LL << (l-1)); // number of nodes in layer l
	ll pos = K + 1 - n; // pos in layer l
	ll x = (1LL << (L-l-1)) - 1; // init pair x,y
	ll y = x;
	ll nleaves = N + 1 - (1LL << (L-1));


	// cout << endl;
	// cout << "L:"<< L << " l:" << l << " nodes:" << n << " pos:" << pos << " nleaves:"<< nleaves <<endl;
	// cout << "init: " << x << " " << y << endl;

	ll add = nleaves/n;
	if (add % 2 == 0){
		x+= add/2;
		y+= add/2;
	}
	else{
		x+= add/2;
		y+= add/2 + 1;
	}

	
	nleaves -= (nleaves/n)*n;
	if (pos <= nleaves){
		x += 1;
	}
	if( y > x )
		swap(x,y);
	
	cout << x << " " << y << endl;
	return;
	
}

int main(){
	int T;
	cin >> T;
	ll N, K;
	for (int i = 0; i < T; ++i)
	{
		cin >> N >> K;
		testcase(i+1, N, K);
	}

	return 0;
}