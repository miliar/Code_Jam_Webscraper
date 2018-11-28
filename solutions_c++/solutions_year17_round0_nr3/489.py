// CodeJam 2017
// Problem C
// zintrepid

#include <iostream>
#include <string>
#include <tuple>
#include <map>

using namespace std;

using SpaceMap = map<uint64_t, uint64_t>;  // Span, Num

bool DoRun()
{
    uint64_t n, k;
    cin >> n >> k;
    if (cin.fail()) return false;
 
    SpaceMap spaceMap;
    spaceMap[n] = 1;
    k -= 1;
    while (k >= spaceMap.rbegin()->second) {
        auto c = *spaceMap.rbegin();
        if (c.first % 2 == 1) {
            spaceMap[c.first / 2] += 2 * c.second;
        } else {
            spaceMap[c.first / 2] += c.second;
            spaceMap[c.first / 2 - 1] += c.second;
        }
        k -= c.second;
        spaceMap.erase(c.first);
    }
    
    uint64_t m = spaceMap.rbegin()->first;
    
    cout << m / 2 << " " << (m-1)/2;
 
    return true;
}

int main()
{
    int runs;
    cin >> runs;
    for (int i=0; i < runs; ++i) {
        cout << "Case #" << i + 1 << ": ";
        if (!DoRun()) {
            cerr << "RUN FAILED\n";
            return 1;
        }
        cout << "\n";
    }
    cerr << "Success.\n";
    return 0;
}
