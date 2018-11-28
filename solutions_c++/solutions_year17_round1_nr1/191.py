#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>

#define D(x) x

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
	os << "[";
	for (int i = 0; i < vec.size(); i++) {
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
    	int R, C;
    	cin >> R >> C;

    	vector<string> grid(R);
    	for (int i = 0; i < R; i++) {
    		cin >> grid[i];
    	}

    	for (int i = 0; i < R; i++) {
    		bool empty = true;
    		for (int j = 0; j < C; j++) {
    			if (grid[i][j] != '?') empty = false;
    		}

    		if (empty) continue;

    		for (int j = 0; j < C; j++) {
    			if (grid[i][j] != '?') continue;

    			for (int j2 = j-1; j2 >= 0; j2--) {
    				if (grid[i][j2] != '?') {
    					grid[i][j] = grid[i][j2];
    					break;
    				}
    			}
    			if (grid[i][j] != '?') continue;
				
				for (int j2 = j+1; j2 < C; j2++) {
    				if (grid[i][j2] != '?') {
    					grid[i][j] = grid[i][j2];
    					break;
    				}
    			}
    		}
    	}

    	for (int i = 0; i < R; i++) {
    		for (int j = 0; j < C; j++) {
    			if (grid[i][j] != '?') continue;

    			for (int i2 = i-1; i2 >= 0; i2--) {
    				if (grid[i2][j] != '?') {
    					grid[i][j] = grid[i2][j];
    					break;
    				}
    			}
    			if (grid[i][j] != '?') continue;

    			for (int i2 = i+1; i2 < R; i2++) {
    				if (grid[i2][j] != '?') {
    					grid[i][j] = grid[i2][j];
    					break;
    				}
    			}
			}
    	}


    	
        cout << "Case #" << testCase << ":" << endl;

        for (int i = 0; i < R; i++) {
        	cout << grid[i] << endl;
        }
    }
}
