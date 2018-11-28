#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define ll unsigned long long

#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 10010
#define MOD 1000000007

using namespace std;

typedef pair<ll, int> pii;

int main (){
	
	queue<pii> q;
	rep(i, 9) q.push(pii(i+1, 1));
	
	vector <ll> tidy;
	while(true){
		pii atual = q.front();
		ll k = atual.first;
		tidy.push_back(k);
		q.pop();

		if(atual.second > 18) break;
		
		for(ll x = k%10; x<10; x++)
			q.push(pii(k*10LLU + x, atual.second+1));
	}
	
	int t;
	scanf("%d", &t);
	
	int Case = 1;
	
	while(t--){
		printf("Case #%d: ", Case++);
		ll n;
		scanf("%llu", &n);
		int pos = upper_bound(all(tidy), n) - tidy.begin();
		if(tidy[pos] > n) pos--;
		printf("%llu\n", tidy[pos]);
	}
	
	return 0;
}
