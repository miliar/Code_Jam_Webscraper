#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <limits>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define all(c) (c).begin(),(c).end()

using namespace std;

typedef long long llong;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int caseNum=1;

#define gout cout << "Case #" << caseNum++ << ": ", cout

int main (int argc, char* argv[]) {
    int T;
    cin >> T;

    while (T--) {
        long long N, K;
        cin >> N;
        cin >> K;

        vector<llong> numbers;

        numbers.push_back(N);

        for (int a=0; a<K; a++) {
            int i=-1;
            llong bestMin = N;
            llong bestMax = -1;
            for (int j=0; j<numbers.size(); j++) {
                llong num = numbers[j];

                llong min = num/2;
                if ((num%2) == 0)
                    min--;
                llong max = num/2;

                bool replace = false;
                if (min < bestMin) {
                    replace = true;
                }
                if (min == bestMin) {
                    if (max > bestMax)
                        replace = true;
                }
                if (replace) {
                    bestMin = min;
                    bestMax = max;
                    i = j;
                }
            }

            int num = numbers[i];
            numbers.erase(numbers.begin()+i);
            if (bestMax > 0)
                numbers.insert(numbers.begin()+i, bestMax);
            if (bestMin > 0)
                numbers.insert(numbers.begin()+i, bestMin);

            if (a == K-1) {
                gout << (bestMax) << " " << bestMin << endl;

                for (int i=0;i<numbers.size();i++) {
                    cout << numbers[i] << ",";
                }
                cout << endl;
            }
        }
    }

    return 0;
}
