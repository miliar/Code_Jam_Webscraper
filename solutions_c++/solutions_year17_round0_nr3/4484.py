#include "iostream"
#include "queue"

using namespace std;

const int N = 1e6;

int main() {
	int T; cin >>T;
	int n, k;
	for(int cs{1}; cs <= T; ++cs) {
		cin >>n >>k;
		int l, r, i{1};
		priority_queue<int> q;
		q.push(n);
		while( i <= k ) {
			n = q.top();
			q.pop();
			l = n/2;
			r = n/2;
			if( n%2 == 0  and n != 1) {
				l--;
			}
			q.push(l);
			q.push(r);
			++i;
		}
		cout <<"Case #"<< cs <<": " <<r <<' ' <<l <<endl;
	}
	return 0;
}
