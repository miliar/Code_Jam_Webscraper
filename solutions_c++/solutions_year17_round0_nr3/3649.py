#include <bits/stdc++.h>
#include <functional>
#include <queue>
#include <vector>

using namespace std;
int main(){
	int t;
	cin >> t;
	for(int q = 1; q <= t; q++){
		long long n,k;
		long long a, b;
		cin >> n;
		cin >> k;
		priority_queue<long long> que;
		que.push(n);
		for(int i = 1; i <= k; i++){
			long long x = que.top() - 1;
			que.pop();
			a = x / 2;
			b = x - a;
			que.push(a);
			que.push(b);
		}
		cout << "Case #" << q << ": " << b << " " << a << endl;
	}
	return 0;
}