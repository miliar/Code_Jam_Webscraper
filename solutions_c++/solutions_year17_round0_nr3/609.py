#include <iostream>
#include <sstream>
#include <numeric>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <strings.h>
#include <limits.h>
#include <stdlib.h>
#include <float.h>
#include <strings.h>
#include <string.h>
using namespace std;

int main(){
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		map<unsigned long long, unsigned long long> stallsPerSize;
		unsigned long long N, K;
		cin >> N >> K;
		priority_queue< unsigned long long > pq;
		unsigned long long initial = N;
		stallsPerSize[initial] = 1;
		pq.push(initial);
		unsigned long long entered = 0;
		cout << "Case #" << (t+1) << ": ";
		while(true){
			unsigned long long current = pq.top();
			pq.pop();
			entered += stallsPerSize[current];
			if (entered >= K){
				cout << current / 2 << " " << (current - 1) / 2 << endl;
				break;
			}
			if ((current % 2) == 0){
				unsigned long long newLarge = current / 2;
				unsigned long long newShort = current / 2 - 1;
				if (stallsPerSize[newLarge] == 0){
					pq.push(newLarge);
				}
				stallsPerSize[newLarge] += stallsPerSize[current];
				if (stallsPerSize[newShort] == 0){
					pq.push(newShort);
				}
				stallsPerSize[newShort] += stallsPerSize[current];
			} else {
				unsigned long long newLarge = current / 2;
				if (stallsPerSize[newLarge] == 0){
					pq.push(newLarge);
				}
				stallsPerSize[newLarge] += (stallsPerSize[current] * 2);
			}
		}
	}
}
