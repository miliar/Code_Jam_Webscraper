#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    freopen("OversizedPancakeFlipper.in", "rt", stdin);
    freopen("OversizedPancakeFlipper.out", "wt", stdout);
    
    int numTests;
	cin >> numTests;
    
    for (int i = 0; i < numTests; ++i) {
		int k;
		string s;
		cin >> s;
		cin >> k;
		
		int size = (int) s.size();
		vector <int> pancakes(size, 0);
		
		for (int j = 0; j < size; ++j) {
			if (s[j] == '+') pancakes[j] = 1;
		}
		
		int cnt = 0;
		bool possible = true;
		for (int j = 0; j < size; ++j) {
			if (pancakes[j] == 0) {
				if ((j + k) <= size) {
					for (int p = j; p < (j + k); ++p) pancakes[p] = (pancakes[p] + 1) % 2;
					++cnt;
				} else possible = false;
			}
		}
        
        if (possible)
        	cout << "Case #" << i + 1 << ": " << cnt << endl;
        else 
        	cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
    }
    
    return 0;
}
