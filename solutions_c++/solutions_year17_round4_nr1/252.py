#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 300030;
const ll  MODD = 1000000007;

int A[MAX_N];

int do_case(){
  for(int i=0;i<4;i++) A[i] = 0;
  int n,p; cin >> n >> p;
  for(int i=0;i<n;i++){
    int x; cin >> x;
    A[x%p]++;
  }

  if(p == 2)
    return A[0] + (A[1]+1)/2;

  int ans = A[0];
  int mini = min(A[1],A[p-1]);
  ans += mini;
  A[1] -= mini;
  A[p-1] -= mini;

  if(p == 3)
    return ans + (A[1]+A[2]+2)/3;

  A[1] = max(A[1],A[3]);
  while(A[1] >= 2 && A[2] >= 1){
    ans++;
    A[1] -= 2;
    A[2] -= 1;
  }

  return ans + (A[1]+1)/2 + (A[2]+1)/2;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    cout << do_case() << endl;
    //do_case();
  }
  
  return 0;
}
