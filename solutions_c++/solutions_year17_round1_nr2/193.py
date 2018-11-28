#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

#define D(x)

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (size_t i = 0; i < vec.size(); i++) {
		if (i > 0) os << ", ";
		os << vec[i];
	}
	os << "]";
	return os;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int N, P;
    	cin >> N >> P;

    	vector<int> R(N);
    	for (int i = 0; i < N; i++) {
    		cin >> R[i];
    	}

    	vector<vector<int>> Q(N, vector<int>(P));
    	vector<vector<int>> minServings(N, vector<int>(P));
    	vector<vector<int>> maxServings(N, vector<int>(P));

    	for (int i = 0; i < N; i++) {
    		for (int j = 0; j < P; j++) {
    			cin >> Q[i][j];
    		}
    		sort(Q[i].begin(), Q[i].end());
    		D(cerr << Q[i] << endl);
    		for (int j = 0; j < P; j++) {
    			minServings[i][j] = (10*Q[i][j]-1)/(11*R[i]) + 1;
    			maxServings[i][j] = (10*Q[i][j])/(9*R[i]);
    		}
    	}

    	vector<int> mostServings(P+1);
    	vector<vector<int>> nextAvail(N, vector<int>(P+1));
    	int best = 0;

    	for (int j = 0; j < P; j++) {
    		D(cerr << "j=" << j << endl);
    		if (minServings[0][j] > maxServings[0][j]) continue;
    		D(cerr << "at 0: min=" << minServings[0][j] << " max=" << maxServings[0][j]);
    		for (int prev = 0; prev <= j; prev++) {
    			D(cerr << "  prev=" << prev << endl);
    			if (mostServings[prev] + 1 <= mostServings[j+1]) continue;

    			bool good = true;
    			vector<int> next(N);
    			for (int i = 1; i < N; i++) {
    				next[i] = nextAvail[i][prev];
    				D(cerr << "    i=" << i << " next=" << next[i] << endl);
    				while (next[i] < P && (maxServings[i][next[i]] < minServings[0][j] || minServings[i][next[i]] > maxServings[i][next[i]])) {
    					D(cerr << "    ...next=" << next[i] << " min=" << minServings[i][next[i]] << " max=" << maxServings[i][next[i]] << endl);
    					next[i]++;
    				}
    				D(cerr << "    ...next=" << next[i] << " min=" << minServings[i][next[i]] << " max=" << maxServings[i][next[i]] << endl);
    				if (next[i] >= P || minServings[i][next[i]] > maxServings[0][j]) {
    					good = false;
    					break;
    				}
    			}
    			if (!good) continue;

    			D(cerr << "    found better score of " << mostServings[prev]+1 << endl);
    			D(cerr << "    next=" << next << endl);
    			mostServings[j+1] = mostServings[prev] + 1;
    			for (int i = 1; i < N; i++) {
    				nextAvail[i][j+1] = next[i]+1;
    			}
    		}
    		best = max(best, mostServings[j+1]);
    	}

        cout << "Case #" << testCase << ": " << best << endl;
    }
}
