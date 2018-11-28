#include <iostream>
#include <string>
#include <vector>


using namespace std;

int main() {
	int T, n, k;
	string panString;
	vector<bool> pancakes;
	
	cin >> T;
	
	for (int t = 1; t <= T; ++t) {
		//reading input and transforming it into bool vector
		cin >> panString;
		
		n = panString.size();
		pancakes.resize(n);
		
		int vecIter = 0;
		for (string::iterator strIt = panString.begin(); strIt != panString.end(); ++strIt) {
			if (*strIt == '+') {
				pancakes[vecIter] = true;
			} else {
				pancakes[vecIter] = false;
			}
			++vecIter;
		}
		
		cin >> k;
		        
        //performing greedy algorithm
        int maneuver = 0;
        int i = 0;
        bool tmp;
        bool possible = true;
        
        while (i < n && possible) {
			//find first to flip
			while (i < n && pancakes[i]) ++i;
			
			//flip if possible
			if (i < n) {
				if (n - i < k) {
					possible = false;
				} else {
					for (int j = 0; j < k; ++j) {
						pancakes[i + j] = !pancakes[i + j];
					}
					++maneuver;
				}
			}
		}
		
		if (possible) {
			cout << "Case #" << t << ": " << maneuver << endl;

		} else {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		}
	}
	
	return 0;
}
