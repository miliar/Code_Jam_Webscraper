#include <bits/stdc++.h>

using namespace std;

#define int long long

int32_t main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;
	for(int cont=1; cont <= t; cont++) {
		int n, k, maior, menor;
		cin >> n >> k;
		int r=0;
		map<int,int> m;
		priority_queue<int> pq;
		m[n] = 1;
		pq.push(n);
		while(r < k) {
			int num=pq.top();
			pq.pop();
			maior=menor=num/2;
			if(num%2==0) {
				menor--;
				if(m.count(maior) == 0)
					pq.push(maior);
				m[maior] += m[num];
				if(menor > 0) {
					if(m.count(menor) == 0)
						pq.push(menor);
					m[menor] += m[num];
				}
			}
			else if(maior > 0) {
				if(m.count(maior) == 0)
					pq.push(maior);
				m[maior] += 2*m[num];
			}
			r += m[num];
		}
		cout << "Case #" << cont << ": " << maior << " " << menor << endl;
	}

	return 0;
}

