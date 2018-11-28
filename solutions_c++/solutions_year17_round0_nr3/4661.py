#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int ii = 0; ii < T; ii++){
		int N, K;
		cin >> N >> K;
		
		priority_queue<int> halda;
		halda.push(N);

		int x,tmp;
		for(int i = 0; i < K; i++){
			x = halda.top();

			halda.pop();

			tmp = x/2;
			halda.push(tmp);
			halda.push(x - tmp - 1);
		}


		cout << "Case #" << ii+1 << ": ";
		cout << max(tmp, x-tmp-1) << " " << min(tmp, x-tmp-1);
		cout << "\n";
	}
	return 0;

	
}
