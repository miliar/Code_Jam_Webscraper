#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T = 0;

    cin >> T;

    for (int i = 1; i <= T; i++) {
        unsigned long long int N = 0, K = 0, maxE = 0, minE = 0;

        cout << "Case #" << i << ": ";

        cin >> N >> K;

        if (N != K) {
        	vector<unsigned long long int> parts;

        	parts.push_back(N);

        	for (unsigned long long int j = 1; j <= K; j++) {
        		unsigned long long int p = parts.back();

        		if (!(p % 2)) {
        			maxE = p / 2;
       				minE = p / 2 - 1;
       			}
       			else {
       				maxE = minE = (p - 1) / 2;
       			}

       			parts.pop_back();
       			parts.push_back(minE);
       			parts.push_back(maxE);
       			sort(parts.begin(), parts.end());
        	}
        }

        cout << maxE << ' ' << minE << endl;
    }

    return 0;
}
