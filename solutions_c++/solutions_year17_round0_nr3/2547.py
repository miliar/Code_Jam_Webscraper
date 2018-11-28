#include <vector>
#include <map>
#include <unordered_map>
#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdint.h>
using namespace std;

int main()
{
    string line;
    getline(cin, line);
    int inputCount = stoi(line);
    for (int caseNum = 0; caseNum < inputCount; caseNum++) {
        getline(cin, line);
        istringstream iss(line);
        uint64_t size = 0;
        uint64_t people = 0;
        iss >> size >> people;

        uint64_t i = 0;
        map<uint64_t,uint64_t> counts;
        counts.insert(pair<uint64_t,uint64_t>(size, 1));
        uint64_t a = 0;
        uint64_t b = 0;

        while (i < people) {
            auto maxItr = prev(counts.end());
            uint64_t max = maxItr->first;
            uint64_t count = maxItr->second;
            counts.erase(maxItr);
            a = max / 2;
            b = (max - 1) / 2;
            counts[a] += count;
            counts[b] += count;
            i += count;
            //cout << count << " " << a << " " << b << endl;
        }

        cout << "Case #" << caseNum+1 << ": " << a << " " << b << endl;
    }
}
