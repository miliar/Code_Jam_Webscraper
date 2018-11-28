#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>

int main()
{
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int N, K;
		std::priority_queue<int> pq;
		std::cin >> N >> K;
		pq.push(N);
		for (int j = 0; j < K - 1; ++j)
		{
			int cur = pq.top();
			pq.pop();
			if (1 == cur) {
				continue;
			}
			else if (2 == cur) {
				pq.push(1);
				continue;
			}
			
			//else, remains >= 3
			if (cur & 1) {
				pq.push(cur / 2);
				pq.push(cur / 2);
			}
			else {
				pq.push(cur / 2);
				pq.push(cur / 2 - 1);
			}
		}
		int last = pq.top();
		pq.pop();
		std::cout << "Case #" << i << ": ";
		if (1 == last)
			std::cout << "0 0\n";
		else if (last & 1)
			std::cout << last / 2 << ' ' << last / 2 << std::endl;
		else
			std::cout << last / 2 << ' ' << last / 2 - 1 << std::endl;
		//while(!pq.empty()){
		//	std::cout << " " << pq.top();
		//	pq.pop();
		//}
		//std::cout << std::endl;
	}
	return 0;
}
