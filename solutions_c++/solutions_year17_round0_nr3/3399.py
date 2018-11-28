#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);cout.tie(NULL);

	int T;cin >> T;
	int n,k;
	for(int t=1;t<=T;++t) {
		cin >> n >> k;
		priority_queue<int> pq;
		pq.push(n);
		k--;
		while(k--) {
			int x = pq.top();
			pq.pop();
			pq.push(x/2);
			if(x%2 == 0 && x/2 > 0)
				pq.push(x/2 - 1);
			else
				pq.push(x/2);
		}
		int x = pq.top(),mx = x/2,mn = x%2==0 ? max(0,x/2 - 1) : x/2;
		cout << "Case #"<<t<<": "<< mx <<' '<< mn <<endl;
	}
}
