#include <iostream>
#include <map>
#include <cmath>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 0; i < cases; ++i) {
        int n, k;
        cin >> n >> k;
        map<long long int, long long int> m = map<long long int, long long int>();
        m[n] = 1;
        long long int occupied = 0;
        long long int toSplit = 0;
        long long int min = 0;
        long long int max = 0;
        while (occupied < k) {
            long long int biggestKey = m.rbegin()->first;
            long long int biggestKeyCount = m.rbegin()->second;
            long long int left = (biggestKey - 1) / 2;
            long long int right = biggestKey / 2;
            if (occupied + biggestKeyCount < k) {
                m[left] += biggestKeyCount;
                m[right] += biggestKeyCount;
                m.erase(biggestKey);
            }
            else {
                min = left;
                max = right;
                break;
            }
            occupied += biggestKeyCount;
        }
        cout << "Case #" << i+1 << ": " << max << " " << min << endl;
    }
    return 0;
}
