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
        cin >> s;
        int K;
        cin >> K;
        string s2;
        int N = s.length();

        int count=0;

        for (int i=0; i<s.length(); i++) {
            if (i+K > N)
                break;

            if (s[i] == '+')
                continue;
            for (int j=i; j<i+K; j++) {
                if (s[j] == '+')
                    s[j] = '-';
                else
                    s[j] = '+';
            }
            count++;
        }

        /*
        if (s[N-1] == '-') {
            for (int j=N-K; j<N; j++) {
                if (s[i] == '+')
                    s[i] = '-';
                else
                    s[i] = '+';
                count++;
            }
        }
        */

        bool good=true;
        for (int i=0;i<N;i++) {
            if (s[i] == '-') {
                good=false;
                break;
            }
        }
        if (good)
            gout << count << endl;
        else
            gout << "IMPOSSIBLE\n";
    }

    return 0;
}
