#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
long long ans[2];
set<pair<long long, long long>> S;
void back(long long n, long long k){
	if (S.find(make_pair(n, k)) != S.end())
		return;
	S.insert(make_pair(n, k));
	if (k == 1) {
		long long sm = (n - 1) >> 1, la = n >> 1;
		if (ans[0] > sm || (ans[0]==sm && ans[1]>la)){
			ans[0] = sm;
			ans[1] = la;
		}
	}
	else if (k == 2){
		back(n >> 1, k >> 1);
	}
	else{
		back((n - 1) >> 1, (k - 1) >> 1);
		back(n >> 1, k >> 1);
	}
}
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		S.clear();
		ans[0] = 1LL << 62;
		ans[1] = -(1LL << 62);
		long long n, k;
		scanf("%lld %lld", &n, &k);
		back(n, k);
		printf("Case #%d: %lld %lld\n", test,ans[1],ans[0]);
	}
	return 0;
}
