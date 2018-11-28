#include <bits/stdc++.h>

using namespace std;
#define pr(x) cout << #x << " " << x << endl;
#define LL long long
priority_queue<int> q;
map<LL, LL> M;
LL n, k;
LL ans1, ans2;
LL sum1, sum2;

void calc(){
	M.clear();
	LL y = (n - 1) >> 1;
	LL z = n - 1 - y;
	ans1 = max(y, z);
	ans2 = min(y, z);
	if (k == 1)
		return;	
	sum1 = sum2 = 1;
	LL sum = 1;
	while(true){
		if (sum + sum1 + sum2 >= k){
			if (sum + sum1 >= k){
				y = (ans1 - 1) >> 1;
				z = ans1 - 1 - y;
				ans1 = max(y, z);
				ans2 = min(y, z);
				return;
			}
			y = (ans2 - 1) >> 1;
			z = ans2 - 1 - y;
			ans1 = max(y, z);
			ans2 = min(y, z);
			return;
		}
		sum += sum1 + sum2;
		y = (ans1 - 1) >> 1;
		z = ans1 - 1 - y;
		LL yy = (ans2 - 1) >> 1;
		LL zz = ans2 - 1 - yy;
		M[y] = M[z] = M[yy] = M[zz] = 0;
		M[y] += sum1;
		M[z] += sum1;
		M[yy] += sum2;
		M[zz] += sum2;
		ans1 = max(y, z);
		ans2 = min(yy, zz);
		if (ans1 == ans2){
			sum1 = sum2 = M[ans1] >> 1;
		}
		else{
			sum1 = M[ans1];
			sum2 = M[ans2];
		}
	}

}

int main(){
	int T;
	cin >> T;
	for (int i = 0; i < T; i++){
		cin >> n >> k;
		// q.clear();
		// while(!q.empty())
		// 	q.pop();
 		// 	q.push(n);
		// int x, y, z;
		// for (int j = 0; j < k; j++){
		// 	x = q.top();
		// 	q.pop();
		// 	y = (x - 1) >> 1;
		// 	z = x - 1 - y;
		// 	q.push(y);
		// 	q.push(z);
		// }

		// int ans1 = max(y, z);
		// int ans2 = min(y, z);
		// printf("Case #%d: %d %d\n", i + 1, ans1, ans2);
		calc();
		printf("Case #%d: %lld %lld\n", i + 1, ans1, ans2);
	}
	return 0;
}