#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <queue>
#include <map>
#define maxn 120009
#define maxm 1000009
using namespace std;
long long D;
struct node{
	long long K, S;
	bool operator < (const node &rhs)const{
		return K < rhs.K;
	}
}a[maxn];
int num;
int n;
int main(){
	int cot = 1;
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1B/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1B/A.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	while(tt--){
		scanf("%lld%d", &D, &n);
		for(int i = 1; i <= n; i++){
			cin >> a[i].K >> a[i].S;
		}
		sort(a + 1, a + 1 + n);
		num = 1;
		for(int i = 2; i <= n; i++){
			if(a[i].S < a[num].S){
				a[++num] = a[i];
			}
		}
		n = num;
		double ans = 1e18;
		for(int i = 1; i <= n; i++){
			double t = 1.0 * (D - a[i].K) / a[i].S;
			ans = min(ans, 1.0 * D / t);
		}
		printf("Case #%d: %.8f\n", cot++, ans);
	}
	return 0;
}
