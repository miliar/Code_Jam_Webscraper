#include<bits/stdc++.h>
using namespace std;

long double PI = 3.1415926535897932384626433832795028841971693993751058209749445923;
int n, k;

priority_queue<long double> pq;
vector<pair<int,int> > arr;

void solve (int tc) {
	printf("Case #%d: ",tc);
	scanf("%d%d",&n,&k);
	long double cur = 0, ans = 0;
	arr.clear();
	for(int i=1;i<=n;i++) {
		int A, B;
		scanf("%d%d",&A,&B);
		arr.push_back({A,B});
	}
	sort(arr.begin(), arr.end());
	for(int i=0;i<k;i++) {
		long double tmp = 2 * PI * arr[i].first * arr[i].second;
		cur += tmp;
		pq.push(-tmp);
	}
	ans = max(ans, cur + PI * arr[k-1].first * arr[k-1].first);
	for(int i=k;i<n;i++) {
		long double tmp = 2 * PI * arr[i].first * arr[i].second;
		ans = max(ans, cur + tmp + pq.top() + PI * arr[i].first * arr[i].first);
		cur += tmp;
		pq.push(-tmp);
		cur += pq.top();
		pq.pop();
	}
	while(!pq.empty()) pq.pop();
	printf("%.12Lf\n",ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++) solve(i);
}
