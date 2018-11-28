/*******************************************************************/
/*******************************************************************/
/* Source: Programming Contest UFPS 2017.                          */
/* Problem Category: REPLACE.                                      */
/* Name Problem: REPLACE.			                                */
/* Problem Setter: Gerson Yesid Lázaro.                            */
/* Problem Tester: Gerson Yesid Lázaro.                            */
/* Date: 10-04-2017 (DD-MM-AAAA)                                   */
/* Verdict:  ACCEPTED.                                             */
/*******************************************************************/
/*******************************************************************/

#include <bits/stdc++.h>
using namespace std;

int main () {
  int t;
  long long d, n;
  long long k, s;
  double val, valmax;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> d >> n;
    valmax = 0;
    for(int j = 0; j < n; j++) {
      cin >> k >> s;
      val = (double)(d - k) / (double)s;
      valmax = max(val, valmax);
    }
    printf("Case #%d: %.6lf\n", i, (double)d/valmax);
  }
  return 0;
}