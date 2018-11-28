#include <iostream>
#include <vector>
#include <queue>
#include <algorithm> // sort
#include <utility>
#include <cmath>

typedef long long ll;
using namespace std;

int main(){
  ll T;
  cin >> T;

  for(int i=0; i<T; i++){
    ll N,K;
    cin >> N >> K;

    // O(log N)
    ll crr = N, n1=1, n2=0;

    ll c = 1;
    while(K > c){
      ll nn1,nn2;
      if(crr % 2 == 0){
        // crr=(2n+2)*i, (2n+1)*j -> n  ,n+1, n  ,n i.e. next=n+1, i, i+2j
        nn1  = n1; nn2  = n1 + 2*n2;
      } else {
        // crr=(2n+3)*i, (2n+2)*j -> n+1,n+1, n+1,n i.e. next=n+1, 2i+j, j
        nn1  = 2*n1 + n2; nn2  = n2;
      }
      crr /= 2; n1 = nn1; n2 = nn2;
      K -= c; c *= 2;
    }


    ll final_seg = (n1>=K) ? crr: crr-1;
    ll l = (final_seg-1)/2, r = (final_seg-1)-l;
    cout << "Case #" << i+1 << ": " << r << " " << l << endl;
  }

  return 0;
}
