#include <bits/stdc++.h>

using namespace std;

int main(void){
  ios::sync_with_stdio(false);
  int t, game = 1, n, k, biggest, toput, ansmin, ansmax;
  cin >> t;
  while(t--){
    cin >> n >> k;
    multiset<int> stalls;
    stalls.insert(n);
    while(k){
      biggest = *stalls.rbegin();
      multiset<int>::iterator it = stalls.end();
      it--;
      stalls.erase(it);
      if (biggest%2){
        toput = biggest/2;
        ansmin = toput;
        ansmax = toput;
      }else{
        toput = biggest/2;
        ansmin = toput-1;
        ansmax = toput;
      }
      stalls.insert(ansmin);
      stalls.insert(ansmax);
      //cout << "After next iteration:" << endl;
      //for(int i : stalls)
        //cout << i << " ";
      //cout << endl;
      k--;
    }
    cout << "Case #" << game++ << ": " << ansmax << " " << ansmin << endl;
  }
}
