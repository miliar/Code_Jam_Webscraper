#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>
#include <ctime>
#include <cassert>
#include <cstring>
#include <fstream>

#define FOR(i, a, b) for(int (i)=(a); (i)<(b); (i)++)
#define IFOR(i, a, b) for(int (i)=(a);(i)<=(b);(i)++)
#define RFOR(i, a, b) for(int (i)=(a);(i)>=(b);(i)--)

using namespace std;

int main() {
    int totalcases;
    cin >> totalcases;
    IFOR(casenum, 1, totalcases) {
        printf("Case #%d: ", casenum);
        // solution
        int n, red, orange, yellow, green, blue, violet;
        cin >> n >> red >> orange >> yellow >> green >> blue >> violet;
        // small

        int sumx = red + blue + yellow;
        int maxx = max(red, max(blue, yellow));
        if (maxx > sumx - maxx) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        int rest = sumx - 2 * maxx;
        vector<char> chars;
        int num1, num2;
        if (red == maxx) {
            chars = { 'R', 'Y', 'B' };
            num1 = yellow, num2 = blue;
        }
        else if (yellow == maxx) {
            chars = { 'Y', 'R', 'B' };
            num1 = red, num2 = blue;
        }
        else {
            chars = { 'B','R','Y' };
            num1 = red, num2 = yellow;
        }
        FOR(i, 0, maxx) {
            cout << chars[0];
            if (i < rest)
                cout << chars[1] << chars[2];
            else {
                char idx = (i < num1 ? chars[1] : chars[2]);
                cout << idx;
            }
        }
        cout << endl;



    }
    return 0;
}