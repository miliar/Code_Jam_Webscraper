#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>

using namespace std;

int main() {
    freopen("BathroomStalls.in", "rt", stdin);
    freopen("BathroomStalls.out", "wt", stdout);

    int numTests;
	cin >> numTests;

    for (int i = 0; i < numTests; ++i) {
		int n, k;
		cin >> n >> k;
		
		priority_queue<int> q;
		q.push(n);
		
		for (int j = 1; j < k; ++j) {
			int maxInterval = q.top();
			q.pop();
			if (maxInterval > 0) {
				int minLeft = (maxInterval - 1) / 2;
				int maxLeft = maxInterval - 1 - minLeft;
				
				q.push(minLeft);
				q.push(maxLeft);
			} else break;
		}
		
		int maxInterval = q.top();
		int x = 0, y = 0;
		if (maxInterval > 0) {
			y = (maxInterval - 1) / 2;
			x = maxInterval - 1 - y;
		}

		/*int cnt = (n - k + 1) / k;
		int rem = (n - k + 1) % k;
		if (rem > 0)
			if (k % 2) ++cnt;
			else cnt += rem;

		int y = (cnt - 1) / 2;
		int x = (cnt % 2) ? y : (y + 1);*/
		
		
        
        cout << "Case #" << i + 1 << ": " << x <<  " " << y << endl;
    }
    
    return 0;
}
