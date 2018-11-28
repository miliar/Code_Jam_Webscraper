// Nurbakyt Madibek
// Look at my code! IT'S AWESOME

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cassert>
#include <unordered_map>
#include <bitset>
#include <unordered_set>

using namespace std;

#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define sz(a) (int)((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair < int, int > pi;

const int mod = (int)1e9 + 7;
const int inf = (int)1e9 + 123;
const ll infl = (ll)1e18 + 123;

const int MAX_N = (int)3e5 + 5;

string rowOfPancakes;
int lengthOfTheFlipper;

int minimumNumberOfFlips() {
    cin >> rowOfPancakes >> lengthOfTheFlipper;
    int res = 0;
    for (int index = 0; index < sz(rowOfPancakes); index++) {
        if (rowOfPancakes[index] == '-') {
            if (index + lengthOfTheFlipper - 1 >= sz(rowOfPancakes))
                return -1;
            res++;
            for (int indexUpdate = index; indexUpdate < index + lengthOfTheFlipper; indexUpdate++)
                rowOfPancakes[indexUpdate] = (rowOfPancakes[indexUpdate] == '+' ? '-' : '+');
        }
    }
    return res;
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base :: sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int numberOfTests;
    cin >> numberOfTests;
    for (int testIndex = 1; testIndex <= numberOfTests; testIndex++) {
        cout << "Case #" << testIndex << ": ";
        int numberOfFlips = minimumNumberOfFlips();
        if (numberOfFlips == -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << numberOfFlips << '\n';
    }
    return 0;
}
