/*************************************************************************
     File Name: gcjc-small.cpp
     ID: obsoles1
     PROG: 
     LANG: C++ 
     Mail: 384099319@qq.com 
     Created Time: Sat 08 Apr 2017 01:47:35 AM EDT
 ************************************************************************/
#include<iostream>
#include<queue>
using namespace std;

int main() {
  freopen("C-small-2-attempt0.in", "r", stdin);
  freopen("c-small.out", "w", stdout);
  int t;
  long long n, k;
  cin >> t;
  for (int caseNum = 1; caseNum <= t; ++caseNum) {
    cout << "Case #" << caseNum << ": ";
    priority_queue<int> q;
    cin >> n >> k;
    k--;
    while (k--) {
      q.push(n/2);
      q.push((n - 1)/2);
      n = q.top();
      q.pop();
    }
    //int kk = k, cnt = 0;
    //cout<<k<<endl;
    //k >>= 1;
    //for (; k; k >>= 1) {
      //n >>= 1;
      //cnt++;
    //}
    //cout<<cnt<<endl;
    //k = kk;
    //if (kk == (1<<cnt)) k = kk - 1;
    //cout<<k<<endl;
    //k >>= 1;
    //for (; k; k >>= 1) {
      //n >>= 1;
      //cnt++;
    //}
    if (n&1) cout << (n>>1) << ' ' << (n>>1) << endl;
    else cout << (n>>1) << ' ' << (n>>1) - 1 << endl;
  }
}
