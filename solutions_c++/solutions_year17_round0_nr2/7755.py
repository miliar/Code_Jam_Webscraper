#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
using namespace std;
int main() {
  int t;
  cin>>t;
  for(int i = 1; i <= t; i++) {
    long long int n;
    cin>>n;
    long long int a[100], j = 0;
    long long int temp = n;
    while(temp > 0) {
      a[j++] = temp % 10;
      temp = temp / 10;
    }
    int flag = 0;
    long long int ans = 0;
    for(int k = j - 1; k > 0; k--) {
      if(a[k] > a[k -1]) {
        for(int l = k - 2; l >= 0; l--)
          a[l] = 9;
        int l = 0;
        for(l = k - 1; l < j - 1; l++) {
          if(a[l] - 1 < a [l + 1]) {
            a[l] = 9;
            if(l + 1 == j - 1) {
              a[j - 1] -= 1;
              flag = 1;
              break;
            }
          }
          else {
            flag = 1;
            a[l] = a[l] - 1;
            break;
          }
        }
        if(flag != 1)
          a[l + 1] -= 1;
      }
    }
    for(int k = j - 1; k >= 0; k--)
      ans = ans * 10 + a[k];
    cout<<"Case #"<<i<<": "<<ans<<"\n";
  }
}
