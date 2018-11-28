#include <iostream>
#include <vector>
using namespace std;

#define rep(i, from, to) for(int i = from; i < to; i++)

int main(){
  long long curr, temp1, temp2, temp3, temp4, count1, count2, T, N, K;
  cin >> T;
  rep(t, 0, T){
    cout << "Case #" << t+1 << ": ";
    cin >> N >> K;
    count1 = 1; curr = N; count2 = 0;
    while (count1+count2-1 < K){
      temp1 = curr/2;
      temp2 = (curr-1)/2;
      temp3 = (curr+1)/2;
      temp4 = curr/2;
      if (count1+count2*2-1 >= K){
        cout << temp3 << " " << temp4 << endl;
        break;
      } else if (2*count1+2*count2-1 >= K){
        cout << temp1 << " " << temp2 << endl;
        break;
      } else {
        if (curr%2 == 0) count2 = 2*count2+count1;
        else count1 = 2*count1+count2;
        curr = temp2;
      }
    }
  }
}
