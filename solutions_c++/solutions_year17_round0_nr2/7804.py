#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <iomanip>
using namespace std;
int testcase=1;

int main()
{
  ifstream input("A:\\input.txt");
  ofstream output("A:\\output.txt");
int t;
input>>t;
while(t--)
{
    string ans = "0";
    string s = "";
    input>>s;
    int l = s.length();
    for (int i = l -1 ;i >= 0;--i) {
        if (i+1 < l && s[i] > s[i+1]) {
            for (int j = i+1; j < l;++j) {
                s[j] = '9';
            }
            s[i] = s[i] - 1;
        }
    }
    for (int i = 0;i < l;++i) {
        if (s[i] > '0') {
            ans = s.substr(i);
            break;
        }
    }
    output<<"Case #"<<testcase<<": "<<ans<<endl;

    testcase++;
}
return 0;
}
