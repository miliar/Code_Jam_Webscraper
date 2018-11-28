#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cctype>
#include <cmath>
#include <vector>
#include <sstream>
#include <bitset>
#include <deque>
#include <iomanip>
using namespace std;
#define pr(x) cout << #x << " = " << x << endl;
#define bug cout << "bugbug" << endl;
#define ppr(x, y) printf("(%d, %d)\n", x, y);
#define MST(a,b) memset(a,b,sizeof(a))
#define CLR(a) MST(a,0)
#define SQR(a) ((a)*(a))
#define PCUT puts("\n---------------")

typedef long long ll;
typedef double DBL;
typedef pair<int, int> P;
typedef unsigned int uint;
const int MOD = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3f;
const int maxn = 1e3 + 4;
const int maxm = 1e4 + 4;
const double pi = acos(-1.0);
set<ll> T, S;
map<ll, ll> Cnt;
int main(){
//必须编译过才能交
	int ik, i, j, k, kase;
	freopen("output.txt", "w", stdout);
	scanf("%d", &kase);
	for (ik = 1; ik <= kase; ++ik){
		ll n, K;
		T.clear(); S.clear();
		scanf("%I64d%I64d", &n, &K);
		printf("Case #%d: ", ik);
		if (n == K){
			puts("0 0");
			continue;
		}
		K--;
		T.insert(n);
		while(T.size()){
			auto it = T.end();
			--it;
			ll num = *it;
			T.erase(it);
			S.insert(num);
			if (num & 1 && num != 1) T.insert(num / 2);
			if (num % 2 == 0){
				ll b = num / 2, a = b - 1;
				if (a) T.insert(a);
				T.insert(b);
			} 
		}
		Cnt.clear();
		Cnt[n] = 1;
		for (auto it = S.end(); it != S.begin(); ){
			--it;
			ll num = *it;
			if (num & 1) Cnt[num / 2] += Cnt[num] * 2;
			else{
				Cnt[num / 2] += Cnt[num];
				Cnt[num/2-1] += Cnt[num];
			}
		}
		ll sum = 0;
		for (auto it = Cnt.end(); it != Cnt.begin(); ){
			--it;
//			cout << it->first << ' ' << it->second << endl;
			sum += it->second;
			if (sum > K){
				printf("%I64d %I64d\n", it->first / 2, it->first - it->first/2 - 1);
				break;
			}
		}
	}
	
	return 0;
}

