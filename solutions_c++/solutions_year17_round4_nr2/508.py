#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <deque>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <valarray>
#include <iterator>
using namespace std;

int N, M, C;
vector<int> P, B;

int main(){
  int T;
  cin >> T;
  for(int caze = 1; caze <= T;caze++) {
    
    cout << "Case #" << caze << ": ";
    cin >> N >> C >> M;
    P = B = vector<int>(M);
    vector<int> Ns(N), Cs(C); 
    for(int i = 0; i < M; i++) {
      cin >> P[i] >> B[i];
      Cs[--B[i]]++;
      Ns[--P[i]]++;
    }
    int minimum = *max_element(Cs.begin(), Cs.end());
    sort(P.begin(), P.end());
    for(int i = 0; i < P.size(); i++) {
      while((i + 1) > (P[i] + 1) * minimum) {
        minimum++;
      }
    }
    cout << minimum;
    int a = 0;
    for(int i = 0; i < Ns.size(); i++) {
      a += max(0, Ns[i] - minimum);
    }
    cout << " " << a << endl;

  }
}