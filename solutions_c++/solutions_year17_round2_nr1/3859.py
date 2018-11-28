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
long power(long n);
int main()
{
  ifstream input("A:\\input.txt");
  ofstream output("A:\\output.txt");
int t;
input>>t;
while(t--)
{
    double d;
    int n;
    input>>d>>n;
    double k[n],s[n];
    for (int i = 0;i < n;++i) {
        input>>k[i]>>s[i];
    }

    double time = 0;
    for (int  i = 0;i < n;++i) {
        double time2 = (d - k[i]) / s[i];
        if(time2 > time) {
            time = time2;
        }
    }
    double ans = d / time;
    
    output<<"Case #"<<testcase<<": "<<fixed<<setprecision(6)<<ans<<endl;

    testcase++;
}
return 0;
}
