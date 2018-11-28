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
    int ans = 0;
    string s = "";
    input>>s;
    int k = 0;
    input>>k;
    int l = s.length();
    for (int i = 0;i < l;++i) {
        if (s[i] == '-') {
            ans++;
            for (int j = i;j < i + k && i + k <= l;++j) {
                if (s[j] == '-') {
                    s[j] = '+';
                }
                else {
                    s[j] = '-'; 
                }
            }
        }
    }
    int flag = 0;
    for(int i = 0;i < l;++i) {
        if (s[i] == '-') {
            flag = 1;
            break;
        }
    }
    if (flag == 0) {
        output<<"Case #"<<testcase<<": "<<ans<<endl;
    } else {
        output<<"Case #"<<testcase<<": "<<"IMPOSSIBLE"<<endl;
    }
    testcase++;
}
return 0;
}
