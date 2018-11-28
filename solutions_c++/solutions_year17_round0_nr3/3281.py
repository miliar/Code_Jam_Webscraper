#include<map>
#include<queue>
#include<iostream>
#include<vector>
#include<functional>
using namespace std;

int main() {
	int num;
	cin >> num;
	map<long long int, long long int> left;
	
	for (int i = 0; i < num; i++) {
		left.clear();
		priority_queue<long long int, vector<long long int>, less<long long int> > pq;
		long long int N, K;
		cin >> N >> K;
		--K;
		left[N] = 1;
		pq.push(N);
		while (K > 0) {
			long long int key, val;
			key = pq.top();
			val = left[key];
			pq.pop();
			if (K < val) {
				pq.push(key);
				break;
			}
			else {
				
				long long int larger, smaller;
				larger = key / 2;
				smaller = (key - 1) / 2;
				if (left.find(larger) == left.end()) {
					left[larger] = val;
					pq.push(larger);
				}
				else {
					left[larger] += val;
				}
				if (left.find(smaller) == left.end()) {
					left[smaller] = val;
					pq.push(smaller);
				}
				else {
					left[smaller] += val;
				}
				K -= val;
				left.erase(key);
			}
			
		}
		long long int rest = pq.top();
		//std::cout << pq.top() << endl;
		std::cout << "Case #" << i + 1 << ": " << rest / 2 << " " << (rest - 1) / 2 << endl;
	}


	return 0;
}