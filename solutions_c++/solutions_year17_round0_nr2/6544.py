#include <iostream>
#include <string>
#include <set>
using namespace std;

set<long long> tidy;
void make_tidy(void)
{
  int i, p, r, num;
  for(i = 1; i < 10000; ++i) {
    num = i;
    p = 10;
    while(num > 0) {
      r = num % 10;
      if(p < r) 
        break;
      num /= 10;
      p = r;
    }
    if(num == 0) {
      tidy.insert(i);
    }
  }
}

int main(void)
{
  make_tidy();
  cout << endl;
  int t, tt;
  cin >> tt;
  for(t = 1; t <= tt; ++t) {
    long long n, answer;
    cin >> n;

    long long prev = 1;
    for(set<long long>::iterator it = tidy.begin(); it != tidy.end(); ++it) {
      if(n < *it) {
        break;
      }
      prev = *it;
    }
    answer = prev;

    cout << "Case #" << t << ": " << answer << endl;
  }
  return 0;
}

