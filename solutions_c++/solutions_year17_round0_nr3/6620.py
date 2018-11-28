#include "bits/stdc++.h"
using namespace std;

int getLS(int minA[], int maxA[], bool A[], int n) {

  // cout << "Min: ";
  // for(int i = 1; i < n + 1; ++i) cout << minA[i] << " ";
  // cout << endl << "Max: ";
  // for(int i = 1; i < n + 1; ++i) cout << maxA[i] << " ";
  // cout << endl;
  queue<int> cand;
  int maxi = -1;
  for(int i = 1; i < n + 1; ++i) {
    if(!A[i] && minA[i] > maxi) maxi = minA[i];
  }
  // cout << "Max Min: " << maxi << endl;
  for(int i = 1; i < n + 1; ++i) {
    if(minA[i] >= maxi) cand.push(i);
  }
  int ans = -1;
  maxi = -1;
  while(!cand.empty()) {
    int curr = cand.front(); cand.pop();
    if(maxA[curr] > maxi) {maxi = maxA[curr]; ans = curr;}
  }
  return ans;
}

void update(bool A[], int minA[], int maxA[], int l[], int r[], int idx, int n) {
  int i = idx;
  for(int j = idx; j > 0; --j) {
    if (A[j] && j != idx) break;
    r[j] = idx - j - 1;
  }
  for(int j = idx; j < n +1; ++j) {
    if (A[j] && j != idx) break;
    l[j] = j - idx - 1;
  }
  // cout << "R: ";
  // for(int i = 1; i < n +1; ++i) cout << r[i] << " ";
  // cout << endl << "L: ";
  // for(int i = 1; i < n +1; ++i) cout << l[i]<< " ";
  // cout << endl;
}

int main(int argc, char const *argv[]) {
  int TC;
  int c = 1;
  scanf("%d",&TC);
  while(TC--) {
    int n,k;
    scanf("%d%d",&n,&k);
    bool A[n + 2];
    A[0] = A[n + 1] = 1;
    int minA[n+2];
    int maxA[n+2];
    int l[n+2];
    int r[n+2];
    int m = n - 1;
    for (int i = 1; i < n + 1; ++i) {
      A[i] = 0;
      l[i] = i -1;
      r[i] = m;
      minA[i] = min(i-1, m);
      maxA[i] = max(i-1, m);
      //cout << maxA[i] << " " << minA[i] << endl;
      --m;
    }
    // cout << "R: ";
    // for(int i = 1; i < n +1; ++i) cout << r[i] << " ";
    // cout << endl << "L: ";
    // for(int i = 1; i < n +1; ++i) cout << l[i]<< " ";
    // cout << endl;
    int last;
    for(int i = 0 ; i < k; ++i) {
      for(int i = 1; i < n + 1; ++i) {
        minA[i] = min(l[i],r[i]);
        maxA[i] = max(l[i],r[i]);
      }
      int ocp = getLS(minA, maxA, A,n);
      //cout << "OCP: " << ocp << endl;
      A[ocp] = 1;
      last = ocp;
      update(A,minA,maxA,l,r,ocp,n);
    }
    int x = max(maxA[last],minA[last]);
    int y = min(maxA[last],minA[last]);
    printf("Case #%d: %d %d\n",c++,x,y);

  }
  return 0;
}
