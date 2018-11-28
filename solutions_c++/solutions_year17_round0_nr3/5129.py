#include <iostream>
#include <queue>
#include <vector>
#include <functional>
using namespace std;

int main() {

	int numTests;
	int N;
	int K;


	cin >> numTests;

	for(int i = 0; i < numTests; ++i) {
		cin >> N >> K;
		priority_queue<int> Q;
		Q.push(N);

		int maxLR;
		int minLR;
		for(int k = 0; k < K; ++k) {
			int t = Q.top();

			Q.pop();

			int div = t / 2;
			if(t % 2 == 0) {
				maxLR = div;
		    	minLR = div-1;
			} else {
				maxLR = div;
				minLR = div;
			}

		    Q.push(maxLR);
		    Q.push(minLR);

		}

		cout << "Case #" << i+1  << ": " << maxLR << " " << minLR << endl;
	}




}