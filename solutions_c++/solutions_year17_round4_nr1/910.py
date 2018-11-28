#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>

#define D(x)

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

int matrix[101][101][101][101][5];

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
    	int N, P;
    	cin >> N >> P;

    	vector<int> counts(5);
    	int total = 0;
    	for (int i = 0; i < N; i++) {
    		int Gi;
    		cin >> Gi;
    		counts[Gi % P]++;
    		total += Gi;
    	}

    	memset(matrix, -1, sizeof matrix);
    	matrix[0][0][0][0][0] = 0;

    	vector<int> indices(4);
    	vector<int> nextIndices(4);

    	for (indices[0] = 0; indices[0] <= counts[0]; indices[0]++) {
    		for (indices[1] = 0; indices[1] <= counts[1]; indices[1]++) {
    			for (indices[2] = 0; indices[2] <= counts[2]; indices[2]++) {
    				for (indices[3] = 0; indices[3] <= counts[3]; indices[3]++) {
    					for (int rem = 0; rem < P; rem++) {
    						int value = matrix[indices[0]][indices[1]][indices[2]][indices[3]][rem];
    						if (value < 0) continue;
							D(cerr << "matrix[" << indices << "][" << rem << "] == " << value << endl);

    						for (int index = 0; index < P; index++) {
    							if (indices[index] < counts[index]) {

    								nextIndices = indices;
    								nextIndices[index]++;
    								int nextRem = (rem + index) % P;
    								int nextValue = value;
    								if (rem == 0) nextValue++;
    								int& nextCell = matrix[nextIndices[0]][nextIndices[1]][nextIndices[2]][nextIndices[3]][nextRem];
    								nextCell = max(nextCell, nextValue);
    							}
    						}
    					}
    				}
    			}
    		}
    	}

    	int finalRem = total % P;
    	int best = matrix[counts[0]][counts[1]][counts[2]][counts[3]][finalRem];

        cout << "Case #" << testCase << ": " << best << endl;
    }
}
