#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

typedef unsigned long long ull;

//bool check(ull);

int main()
{
  int T;
  //ull N;
  string N;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> N;

    int k = 0;
    while (N[k] <= N[k+1] && k < N.length()-1)
      k++;

    if (k < N.length()-1)
      N[k]--;
    while (++k < N.length())
      N[k] = '9';
    for (int j = N.length()-1; j > 0; --j) {
      if (N[j] < N[j-1]) {
        N[j] = '9';
        N[j-1]--;
      }
    }
    
    int j = 0;
    while (N[j] == '0')
      ++j;

    cout << "Case #" << i << ": ";
    while (j < N.length())
      cout << N[j++];
    cout << endl;
    
  }

  return 0;
}

    /*
    while (!check(N))
      N--;

    cout << "Case #" << i << ": " << N << endl;
    
bool check(ull N)
{
  bool yes = true;
  int before = N % 10;
  N /= 10;
  
  while (N && yes) {
    int curr = N % 10;
    if (before < curr)
      yes = false;
    before = curr;
    N /= 10;
  }

  return yes;
}
    */
