#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
  
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
  
using namespace std;
  
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
  
const int INF=1<<29;
const double EPS=1e-9;
  
const int dx[]={1,0,-1,0,1,1,-1,-1},dy[]={0,-1,0,1,1,-1,-1,1};


int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string N;
        cin >> N;
        stringstream ss;
        for (int i = N.size() - 1; i >= 1; i--) {
            if (N[i] < N[i - 1]) {
                for (int j = i; j < N.size(); j++) {
                    N[j] = '9';
                }
                N[i - 1]--;
            }
        }
        ss << N;
        long long int ans;
        ss >> ans;
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
    return 0;
}
