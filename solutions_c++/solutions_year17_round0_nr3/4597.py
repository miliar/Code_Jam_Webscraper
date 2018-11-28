#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main() {
	int n, k, t;
	cin >> t;
	for(int i = 0; i < t; i++){
		priority_queue<int> myq;
		cin >> n >> k;

		myq.push(n);

		for(int j=k;j>1;j--) {
			int mytmp = myq.top();
			myq.pop();
			myq.push(ceil((mytmp-1)/2.0));
			myq.push(floor((mytmp-1)/2.0));
		}
		cout << "Case #" << i+1 << ": " << ceil((myq.top()-1)/2.0) << " " << floor((myq.top()-1)/2.0) << endl;
	}

	return 0;
}

