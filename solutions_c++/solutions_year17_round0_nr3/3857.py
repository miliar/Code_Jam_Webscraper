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
        int N, K;
        cin >> N >> K;

        priority_queue<int> q;
        q.push(N);
        for (int i = 0; i < K - 1; i++) {
            int x = q.top(); q.pop();
            if (x % 2 == 0) {
                q.push((x - 1) / 2);
                q.push((x - 1) / 2 + 1);    
            } else {
                q.push((x - 1) / 2);
                q.push((x - 1) / 2);
            }
        }
        int x = q.top(); q.pop();
        int mi, ma;
        if (x % 2 == 0) {
            mi = (x - 1) / 2; 
            ma = (x - 1) / 2 + 1;
        } else {
            mi = (x - 1) / 2; 
            ma = (x - 1) / 2;
        }
        cout << "Case #" << t + 1 << ": " << ma << " " << mi << endl;
    }
    return 0;
}