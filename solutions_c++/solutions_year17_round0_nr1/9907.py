using namespace std;
#include <bits/stdc++.h>

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define INF 1000000000
#define DEBUG(x) cout << "-> " << #x << " = " << x << "\n";

vector<bool> flip(vector<bool> pancakes, int start, int length) {
	vector<bool> returnPancakes = pancakes;
	for(int i = start; i < start + length; i++) {
		if(returnPancakes[i] == false) {
			returnPancakes[i] = true;
		} else {
			returnPancakes[i] = false;
		}
	}
	return returnPancakes;
}
int main() {
	//ios_base::sync_with_stdio(0);
	//cin.tie(0);

	/* No problem can withstand the assault of sustained thinking */

	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++) {
		string pancakes;
		int size;
		cin >> pancakes >> size;

		int pancakeLength = pancakes.length();

		queue <pair<int, vector<bool> > > pancakeQueue;

		vector<vector<bool> > familiars;

		vector<bool> pancakesSet;
		for(int a = 0; a < pancakeLength; a++) {
			pancakesSet.push_back(pancakes[a] == '+');
		}

		pancakeQueue.push(make_pair(0, pancakesSet));
		familiars.push_back(pancakesSet);
		bool shouldContinue = true;
		int theResult = -1;

		if(find(pancakesSet.begin(), pancakesSet.end(), false) == pancakesSet.end()) {
			shouldContinue = false;
			theResult = 0;
		}
		while(shouldContinue) {
			if(pancakeQueue.empty()) {
				shouldContinue = false;
				continue;
			}
			pair<int, vector<bool> > ourPancake = pancakeQueue.front();
			pancakeQueue.pop();
			int nextLevel = ourPancake.first + 1;
			if(nextLevel == 30){
				shouldContinue = false;
				break;
			}
			//cout << "c";

			for(int x = 0; x < pancakeLength - size + 1; x++) {
				vector<bool> nextPancake = flip(ourPancake.second, x, size);
				if(find(nextPancake.begin(), nextPancake.end(), false) == nextPancake.end()) {
					shouldContinue = false;
					theResult = nextLevel;
					break;
				}
				if (find(familiars.begin(), familiars.end(), nextPancake) != familiars.end()) {
				  continue;
				}
				familiars.push_back(nextPancake);
				pancakeQueue.push(make_pair(nextLevel, nextPancake));
			}
		}

		if(theResult == -1) {
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << theResult << endl;
		}

	}
}
