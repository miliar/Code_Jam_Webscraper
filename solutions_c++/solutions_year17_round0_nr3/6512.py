#include <iostream>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

vector<long int> half(long int a){
	vector<long int> halves;
	halves.push_back((a-1) / 2);
	halves.push_back(a-halves[0] - 1);
	return halves;
}

int main(){
	int count;
	cin >> count;

	for (int i = 0; i < count; i++){
		priority_queue<long int> gaps;
		long int n, k, y, z;
		cin >> n >> k;
		if (n == k){
			z = 0;
			y = 0;
			cout << "Case #" << i + 1 << ": " << y << " " << z << endl;	
			continue;
		}else{
			gaps.push(n);
			for (int j = 1; j < k; j++){
				int top = gaps.top();
				gaps.pop();
				vector<long int> hs = half(top);
				gaps.push(hs[0]);
				gaps.push(hs[1]);
			}
		}
		vector<long int> res = half(gaps.top());
		y = res[1];
		z = res[0];
		cout << "Case #" << i + 1 << ": " << y << " " << z << endl;		
	}
	return 0;
}
