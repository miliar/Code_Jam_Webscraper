#include <bits/stdc++.h>
#define endl '\n'
#define Int long long
#define pb push_back
#define mp make_pair
using namespace std;

struct Interval {
	int from, to, l, s, len;

	Interval(){}
	Interval(int from, int to) {
		this->from = from;
		this->to = to;
		len = to - from + 1;
		
		if(len % 2 == 0) {
			l = len / 2 - 1;
			s = len / 2;
		}
		else {
			l = len / 2;
			s = len / 2;
		}
	}		

	bool operator< (const Interval &other) const {
		if(min(l, s) != min(other.l, other.s)) {
			return min(l, s) < min(other.l, other.s); 
		}
		else {
			if(max(l, s) != max(other.l, other.s)) {
				return max(l, s) < max(other.l, other.s);
			}
			else {
				return from > to;
			}
		}
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int cnt_tests;
	cin>>cnt_tests;

	for(int cs = 1; cs <= cnt_tests; cs++) {
		int n, k;
		cin>>n>>k;

		cout<<"Case #"<<cs<<": ";

		if(n == k) {
			cout<<0<<" "<<0<<endl;
			continue;
		}

		priority_queue<Interval> pq;
		pq.push(Interval(1, n));
	
		for(int i = 0; i < k - 1; i++) {
			//cout<<pq.top().from<<" "<<pq.top().to<<endl;
			
			if(pq.empty()) {
				break;
			}

			Interval tmp = pq.top();

			pq.pop();
			if(tmp.from + tmp.l - 1 > tmp.from) {
				pq.push(Interval(tmp.from, tmp.from + tmp.l - 1));
			}
			if(tmp.from + tmp.l + 1 < tmp.to) {
				pq.push(Interval(tmp.from + tmp.l + 1, tmp.to));
			}
		}
		
		if(pq.empty()) {
			cout<<"0 0"<<endl;
			continue;
		}

		cout<<max(pq.top().l, pq.top().s)<<" "<<min(pq.top().l, pq.top().s)<<endl;
	}
}
