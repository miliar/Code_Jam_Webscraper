#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  long long n, k, n_l, n_r, p_now, p_large, p_small;
  for (int t = 1; t<=T; t++) {
    cin >> n >> k;
    p_now = n;
    long long base = 1, now_k = k;
    while (now_k>0) {
      // cout<<"i k p_now p_left base: "<<i<<" "<<k<<" "<<p_now<<" "<<p_left<<" "<<base<<endl;
      // cout<<p_now<<" "<<now_k<<" "<<endl;
      now_k--;
      if (p_now%2==1) {
        n_l = n_r = p_now/2;
        now_k = now_k/2 + now_k%2;
        p_now = n_l;
      }
      else {
        n_l = p_now/2 - 1;
        n_r = p_now/2;
        if (now_k%2==1) {
          p_now = n_r;
          now_k = now_k/2 + now_k%2;
        }
        else {
          p_now = n_l;
          now_k = now_k/2;
        }
      }
      p_large = n_l>n_r?n_l:n_r;
      p_small = n_l<n_r?n_l:n_r;
      // cout<<p_large<<" "<<p_small<<"\n--------------"<<endl;
    }
    cout<< "Case #"<<t<<": "<<p_large<<" "<<p_small<<endl;
  }
  return 0;
}