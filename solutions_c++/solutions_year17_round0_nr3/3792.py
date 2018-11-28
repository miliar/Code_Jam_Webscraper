#include <iostream>
#include <queue>
using namespace std;
int main(){
	int t = 0, maxT, n, k;
	cin >> maxT;
	while (t < maxT) {
		t++;
		priority_queue <int> q;
		cin >> n >> k;
		q.push(n);
		int a, b, r;
		for (int i = 0; i < k; i++) {
			r = q.top() - 1;
			q.pop();
			a = (int)((r + 1) / 2);
			b = (int)(r / 2);
			q.push(a);
			q.push(b);
		}
		cout << "Case #" << t << ": " << a << " " << b << endl;
	}
	return 0;
}
