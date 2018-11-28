#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#define MAXX 1100
#define pb push_back
#define CLR(x) memset(x, 0, sizeof(x))
#define all(x) x.begin(), x.end()

using namespace std;
vector <int> digits;
int mynum[20];

int main(){

  int kases, i, j;
  long long N;

  freopen("io/gcj17b_big_in.txt", "r", stdin);
  freopen("io/gcj17b_big_out.txt", "w", stdout);

  cin >> kases;

  for(int i = 0; i < kases; i++){
    cin >> N;

    digits.clear();
    for(int j= 0; j < 20; j++){
      mynum[j] = 9;
    }

    while(N > 0LL){
      digits.pb(N%10LL);
      N /= 10LL;
    }

    reverse(all(digits));
    int num_digits = digits.size();

    for( j = 1; j < num_digits; j++){
      if(digits[j] < digits[j-1]){
        int p = j-1;
        while(p > 0 && digits[p] == digits[p-1]){
          p--;
        }
        digits[p]--;
        p++;
        for(; p < num_digits; p++){
          digits[p] = 9;
        }
        break;
      }
    }

    long long int ans = 0LL;
    for( j = 0; j < num_digits; j++){
      ans = ans * 10LL + (long long)digits[j];
    }

    cout <<"Case #"<<i+1<<": "<< ans << endl;
  }

  return 0;
}
