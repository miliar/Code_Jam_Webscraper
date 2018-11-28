#include <iostream>
#include <queue>
#include <list>
#include <stdio.h>
#include <stdlib.h>




using namespace std;

int main() {
	int T;

	cin >> T;

	for (int ii = 0; ii < T; ii++) {
		printf("Case #%d: ", ii + 1);


		int N, K;
		cin >> N >> K;

		priority_queue<int> gaps;
		gaps.push(N);

		for (int i = 1; i < K; i++) {
			int gap = gaps.top();
			gaps.pop();

			gaps.push(gap / 2);
			gaps.push(gap - gap / 2 - 1);
		}

		int gap = gaps.top();
		printf("%d %d\n", gap / 2, gap - gap / 2 - 1);
	}
}





















// struct compare {
//     bool operator()(pair<int, int> &lhs, 
//                     pair<int, int> &rhs) const {
//     	int minl = min(lhs.first, lhs.second);
//     	int maxl = max(lhs.first, lhs.second);
//     	int minr = min(rhs.first, rhs.second);
//     	int maxr = max(rhs.first, rhs.second);

//     	if (minl < minr) {
//     		return true;
//     	} else if (minl > minr) {
//     		return false;
//     	} else {
//     		if (maxl > maxr) {
//     			return true;
//     		} else {
//     			return false;
//     		}
//     	}
//     }
// };

// int main() {
// 	int T;
// 	cin >> T;

// 	for (int Ti = 0; Ti < T; Ti++) {
// 		cout << "Case #" << Ti + 1 << ": ";
// 		priority_queue<int, vector<pair<int, int> >, compare> pq;

// 		int N, K;
// 		cin >> N;
// 		cin >> K;

// 		K--;
// 		pq.push(make_pair(N / 2, N - (N / 2) - 1));
// 		if (K == 0) { 
// 			cout << N/2 << " " << N - N/2 - 1<< endl;
// 			continue;
// 		}

// 		while (K > 1) {
// 			pair<int, int> p = pq.top();
// 			pq.pop();



// 			K--;
// 		}	


// 		cout << endl;
// 	}
// }


