#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int test;
	cin >> test;
	for(int ctr=1;ctr<=test;ctr++) {
		priority_queue<int> q;
		long long n,k;
		cin >> n >> k;
		k--;
		q.push(n);
		while(k--) {
			int res = q.top()-1;
			q.pop();
			int a = res/2, b = res/2;
			if(res%2) a++;
			q.push(a);
			q.push(b);
		}
		int a = (q.top()-1)/2, b = (q.top()-1)/2;
		if((q.top()-1)%2) a++;
		cout << "Case #" << ctr << ": " << a << " " << b << "\n";
	}
	return 0;
}