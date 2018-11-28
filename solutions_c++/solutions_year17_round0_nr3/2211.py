#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define INF 2000000000
#define pb push_back
#define fs first
#define sc second
#define mp make_pair

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
typedef vector < int > VI;
typedef vector < unsigned int > VUI;
typedef vector < string > VS;
typedef vector < pair < int, int > > VII;


int main (int argc, char** argv) {
    
    // freopen(argv[1], "rt", stdin);
    // freopen(".out", "wt", stdout);

    int T;
    cin >> T;
    ULL n, k;

    for (int t = 0; t < T; ++t) {
    	cin >> n >> k;

    	ULL old = 0;
    	ULL countMin = 1;
    	ULL countMax = 0;
    	ULL numMin = n;
    	ULL numMax = n;
    	ULL temp;

    	while (old + countMin + countMax < k) {
    		old += countMin + countMax;
    		
    		if (numMin % 2 == 1 && numMax % 2 == 0) {
    			numMin = numMin / 2;
    			numMax = numMax / 2;

    			countMin = 2 * countMin + countMax;
    			countMax = countMax;
    		}
    		else if (numMin % 2 == 1 && numMax % 2 == 1) {
    			numMin = numMin / 2;
    			numMax = numMax / 2;

    			temp = countMin;
    			countMin += countMax;
    			countMax += temp;
    		}
    		else if (numMin % 2 == 0 && numMax % 2 == 0) {
    			numMin = numMin / 2 - 1;
    			numMax = numMax / 2;

    			temp = countMin;
    			countMin += countMax;
    			countMax += temp;
    		}
    		else if (numMin % 2 == 0 && numMax % 2 == 1) {
    			numMin = numMin / 2 - 1;
    			numMax = numMax / 2;

    			countMin = countMin;
    			countMax = countMin + 2 * countMax;
    		}

    		//cout << countMin << " " << countMax << " --- " << numMin << " " << numMax << endl;
    	}

    	if (old + countMax >= k) {
    		cout << "Case #" << t+1 << ": " << numMax / 2 << " " << numMax / 2 - (numMax % 2 == 0 ? 1 : 0) << endl;
    	} else {
    		cout << "Case #" << t+1 << ": " << numMin / 2 << " " << numMin / 2 - (numMin % 2 == 0 ? 1 : 0) << endl;
    	}

    }

    return 0;
}
