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

    string s;
    getline(cin,s);

    while (T--) {
        getline(cin,s);

        int last = s.size()-1;

        for (int i=s.size()-1; i>=1; i--) {
            int c2 = s[i];
            int c1 = s[i-1];
            if (c2 < c1) {
                last = i-1;
                s[last]--;
            }
        }

        gout << "";
        for (int i=0; i<=last; i++) {
            if (s[i] == '0')
                continue;
            cout << s[i];
        }
        for (int i=0; i<(s.size()-last-1); i++)
            cout << '9';
        cout << endl;
    }

    return 0;
}
