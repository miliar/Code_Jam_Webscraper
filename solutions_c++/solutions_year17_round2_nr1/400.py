#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
  int numTests;
  cin >> numTests;
  for (int test = 1; test <= numTests; test++) {
    long long D, N, Ki, Si;
    cin >> D >> N;
    double time = 0;
    for (int i = 0; i < N; i++) {
      cin >> Ki >> Si;
      if ((D - Ki) / (double) Si > time)
        time = (D - Ki) / (double) Si;
    }
    printf("Case #%d: %.8lf\n", test, D / time);
  }
}
