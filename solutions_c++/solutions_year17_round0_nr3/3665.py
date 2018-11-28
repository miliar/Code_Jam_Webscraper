#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

void print_heap(vector<int> v){
	for (unsigned i=0; i<v.size(); i++)
    	std::cout << ' ' << v[i];

  	std::cout << '\n';
}

int main(){
	int numOfCases;
	cin >> numOfCases;
	for (int cases = 1; cases <= numOfCases; cases++){
		int n, k;
		cin >> n;
		cin >> k;
		if (n <= k){
			cout << "Case #" << cases << ": 0 0" << "\n";
			continue;
		}
		priority_queue<int> q;
		q.push(n);
		for (int i = 0; i < k - 1; i++) {
			int max_ele = q.top();
			q.pop();
			if (max_ele % 2 == 0){
				q.push(max_ele/2);
				if (max_ele >= 2) {
					q.push(max_ele/2 - 1);
				}
			} else if (max_ele - 1 > 0) {
				q.push((max_ele - 1)/2);
				q.push((max_ele - 1)/2);
			}
		}
		int max_ele = q.top();
		q.pop();
		cout << "Case #" << cases << ": ";
		if (max_ele % 2 == 0){
			cout << max_ele/2 << " " << max_ele/2 - 1 << "\n";
		} else {
			cout << (max_ele - 1)/2 << " " << (max_ele - 1)/2 << "\n";
		}
	}
	return 0;
}