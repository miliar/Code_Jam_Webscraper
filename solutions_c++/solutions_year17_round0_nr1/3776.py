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
        string S;
        int K;
        cin >> S >> K;
        int count = 0;
        for (int i = 0; i < S.size() - K + 1; i++) {
            if (S[i] == '-') {
                count++;
                for (int j = 0; j < K; j++) {
                    S[i + j] = S[i + j] == '+' ? '-' : '+'; 
                }
            }
        }
        bool flag = true;
        for (int i = 0; i < S.size(); i++) {
            if (S[i] == '-') {
                flag = false;
                break;
            }
        }
        if (flag) {
            cout << "Case #" << t + 1 << ": " << count << endl;
        } else {
            cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}