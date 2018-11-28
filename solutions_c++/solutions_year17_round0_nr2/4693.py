#include <bits/stdc++.h>
#define ll long long

using namespace std ;

int main(int argc, char const *argv[])
{
  ll count;
  cin >> count ;
  for (int j = 0; j < count; ++j) {
    cout << "Case #" << j+1 <<": " ;
    string num;
    ll i {0};
    cin >> num ;
    if (num.size() == 1) {
      cout << num << endl;
      continue;
    }
    for (i = 0 ; i < num.size() - 1; i++) {
      if (num[i] > num[i + 1])
        break;
    }
    if(i == (num.size() - 1)) {
      i--;
    }
    if (num[i] <= num[i+1] ) {
      cout << num << endl;
      continue;
    }
    if (num[i] == '1') {
      for (i = 0; i < num.size() - 1; i++) {
        cout << '9';
      }
      cout << endl;
      continue;
    }
    ll temp {i};
    char c {num[i]};
    char nc {num[i] - 1};
    while (num[temp - 1] == c ) {
      num[temp] = '9';
      temp--;
    }
    num[temp] = nc;
    for (ll j = i + 1 ; j < num.size(); j++) {
      num[j] = '9';
    }
    cout << num << endl;
  }
  return 0;
}
