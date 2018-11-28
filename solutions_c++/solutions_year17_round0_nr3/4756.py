#include<iostream>
#include<cstdlib>
#include<queue>

using namespace std;

int main() {
	int test;
	cin >> test;
	for(int t=1; t<=test; ++t) {
		int k, n;
		cin >> n >> k;
		priority_queue<long long> q;
		q.push(n);
		long long left = 0;
		long long right= 0;
		for(int i=0; i<k; ++i) {
			long long val = q.top();
			q.pop();
			val -= 1;
			left = val/2;
			right = val/2;
			if(val%2 != 0)
				left += 1; 
			q.push(left);
			q.push(right);
		}
		cout << "Case #" << t << ": " << left << " " << right << endl;

	}
	return 0;
}
