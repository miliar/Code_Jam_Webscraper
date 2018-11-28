#include <iostream>
#include <stdint.h>
#include <string>
#include <queue>

using namespace std;

void solve(uint64_t N, uint64_t K)
{
	uint64_t max_v, min_v;
	priority_queue<uint64_t> pq;
	pq.push(N);
	
	while((pq.top() > 0) && K > 0) {
		uint64_t temp = pq.top();
		pq.pop();
		max_v = temp / 2;
		if((temp & 0x1) == 0x1) {
			min_v = max_v;		
		} else {
			if(max_v > 0) {
				min_v = max_v - 1;
			} else {
				min_v = 0;
			}
		}
		pq.push(max_v);
		pq.push(min_v);
		K--;
	}
	cout << max_v << " " << min_v;
}

int main(void)
{
	int Num, i;
	cin >> Num;

	for(i=0; i<Num; i++) {
		uint64_t N, K;
		cin >> N >> K;
		cout << "Case #" << i + 1 << ": ";
		solve(N, K);
		cout << endl;
	}
}