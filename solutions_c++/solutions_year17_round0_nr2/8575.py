/*#include<iostream>
#include<fstream>
#include<set>
#include<map>
#include<unordered_map>
#include<cmath>
#include<cstring>
#include<string>
#include<bitset>
#include<algorithm>
#include<vector>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>*/
#include <bits/stdc++.h>

using namespace std;
//using namespace __gnu_pbds;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
//typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)
#define FORd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i,a) for (int i = (a)-1; i >= 0; i--)

#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound

const int MOD = 1000000007;
double PI = 4*atan(1);

ll get(ll cur, int len, ll N, int clen) {
	if (len == clen) return cur;
	ll cur1 = cur;
	F0R(i,clen-len) cur1 /= 10;
	FORd(i,cur1 % 10,10) {
		ll z = i;
		F0R(j,clen-len-1) z *= 10;
		ll cur1 = cur + z;
		if (cur1 > N) continue;
		ll rec = get(cur1,len+1,N,clen);
		if (rec > -1) return rec;
	}
	return -1;
}

int main() {
    freopen("ben.txt", "w", stdout);
	ios_base::sync_with_stdio(0);cin.tie(0);
	int T; cin >> T;
	F0R(i,T) {
		cout << "Case #" << (i+1) << ": ";
		ll N, N1, clen = 0; cin >> N; N1 = N;
		while (N1) {
			clen ++;
			N1 /= 10;
		}
		cout << get(0,0,N,clen) << "\n";
	}
}
