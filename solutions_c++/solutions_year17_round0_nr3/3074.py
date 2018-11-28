#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef priority_queue<int> PQI;
typedef map<int, int, greater<int>> MII;

const LL MAX_VAL = 100000000000000L;

int main() {
	int tcCount;
	cin >> tcCount;
    
	//process test cases
	for (int tc = 1; tc <= tcCount; ++tc) {
        int size, count;
        cin >> size >> count;

        int max = size, min = size, currSize = size, currCount = 1;
        MII pm;
        pm[size] = currCount;

        do {
            auto head = pm.begin();
            currSize = (*head).first;
            currCount = (*head).second;
            pm.erase(head);
            
            max = currSize >> 1;
            min = (currSize - 1) >> 1;

            if ((currSize & 1) == 1) {
                pm[max] += currCount << 1;
            } else {
                pm[max] += currCount;
                pm[min] += currCount;
            }
            count -= currCount;
        } while (count > 0);
        
        cout << "Case #" << tc << ": " << max << " " << min << endl;
	}

	return 0;
}
