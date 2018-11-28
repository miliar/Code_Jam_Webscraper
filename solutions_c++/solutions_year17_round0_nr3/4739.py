#include <bits/stdc++.h>
using namespace std;
typedef long long int ULLI;
int main(int argc, char const *argv[])
{
	int test,case_no = 1;
	scanf("%d", &test);
	while(test--) {
		ULLI n,k;
		scanf("%lld %lld", &n, &k);
		priority_queue<pair<ULLI, pair<ULLI,ULLI> > > q;

		// Insert in queue
		q.push(make_pair(n+1-0-1, make_pair(0, n+1)));
		while(k > 1) {
			k--;
			pair<ULLI,ULLI> p = q.top().second;
			q.pop();
			ULLI val = p.first + (p.second - p.first)/2;
			q.push(make_pair(val - p.first - 1, make_pair(p.first, val)));
			q.push(make_pair(p.second - val - 1, make_pair(val, p.second)));
		}
		// Record the value of last person
		pair<ULLI,ULLI> p = q.top().second;
		q.pop();
		ULLI high,low;
		ULLI val = p.first + (p.second - p.first)/2;

		high = max(val - p.first - 1, p.second - val - 1);
		low  = min(val - p.first - 1, p.second - val - 1);

		// Print the values
		printf("Case #%d: %lld %lld\n",case_no++, high, low);
	}
	return 0;
}