#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <map>
#include <math.h>
#include <queue>
#include <climits>
#include <iomanip>

using namespace std;

void solution(const string& s, long long k)
{
    char l = '-';
    size_t count = 0;
    queue<long long> exitPoint;

    for (int i = 0; i < s.size(); ++i) {
        if (exitPoint.size() && exitPoint.front() == i) { 
            l = (l == '-') ? '+' : '-';
            exitPoint.pop();
        }

        if (s[i] == l) {
            if (i + k > s.size()) {
                cout << "IMPOSSIBLE" << endl;
                return;
            } else {
                count++;
                l = (l == '-') ? '+' : '-';
                long long changed_index = i + k;
                exitPoint.push(changed_index);
            }
        } 
    }

    cout << count << endl;
}

int main()
{
    int T;
    cin >> T;

    for (size_t i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        string input;
        long long k;
        cin >> input >> k;
        solution(input, k);
    }
    return 0;
}
