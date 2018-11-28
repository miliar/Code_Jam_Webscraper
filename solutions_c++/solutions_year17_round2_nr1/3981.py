#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>


using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    int T,N;
    long int D;
    cin >> T;
    vector<long int> K;
    vector<long int> S;
    vector<double> t;
    for(int tc=1;tc <= T;tc++){
      cout << "Case #" << tc << ": ";
      cin >> D; cin >> N;
      K.resize(N); S.resize(N); t.resize(N);
      for (int i=0;i<N;i++){
        cin >> K[i]; cin >> S[i];
        t[i] = double((D-K[i])/S[i]) + ((D-K[i])%S[i])/double(S[i]);
      }
      double max=t[0];
      for (int j=1;j<t.size();j++)
        if (max < t[j]) max=t[j];
      double ans = D / max;
      cout << ans << endl;;
      
    }

    return 0;
}



