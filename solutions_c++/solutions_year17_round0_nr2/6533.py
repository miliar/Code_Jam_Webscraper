#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

bool isAscending(int num) {
	vector <int> digs;
	while (num > 0) {
		digs.push_back(num % 10);
		num /= 10;
	}

	reverse(digs.begin(), digs.end());
	for (int i = 1; i < (int) digs.size(); ++i) {
		if (digs[i] < digs[i - 1]) return false;
	}
	return true;
}

int main() {
    freopen("TidyNumbers.in", "rt", stdin);
    freopen("TidyNumbers.out", "wt", stdout);
    
    int numTests;
	cin >> numTests;
    
    for (int i = 0; i < numTests; ++i) {
		int N;
 		cin >> N;
		
		while (!isAscending(N)) {
			--N;
		}
 		       
        cout << "Case #" << i + 1 << ": " << N << endl;
    }
    
    return 0;
}
