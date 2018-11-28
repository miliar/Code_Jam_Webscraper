#include <iostream>
#include <algorithm>
#include <cstring>
#include <queue>
using namespace std;

std::priority_queue<int, std::vector<int>, std::less<int> > q;
int TC, N, K, x;

int main() {
	cin >> TC;
	for(int z = 1; z <= TC; z++) {
		cin >> N >> K;
		q.push(N);
		for(int i = 1; i < K; i++) {
			x = q.top();
			//cout << x << " " << q.size() << endl;
			q.pop();
			q.push(x / 2);
			q.push((x - 1) / 2);
		}
		x = q.top();
		//cout << x << " " << q.size() << endl;
		while(!q.empty())
			q.pop();
		cout << "Case #" << z << ": " << x / 2 << " " << (x - 1) / 2 << endl;
	}
}


