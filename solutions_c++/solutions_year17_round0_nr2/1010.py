// 2014 code jam round 1 Problem A
int v = 0 ;

#include <iostream>
#include <vector>
#include <math.h>
#include <string>
#include <map>
#include <set>
#include <bitset>
using namespace std ;

typedef long long int ll;

int caseNumber ;


////////////////////////////////////////////////////////
// Main program here:

int isTidy(char n[]) {
  ll l = strlen(n);
  int i;
  char c = n[0] ;
  for (i = 1 ; i < l ; i++) {
    if (n[i] < c)
      return 0 ;
    c = n[i];
  }
  return 1;
}

int runTest() {
  char n[2048];
  cin >> n ;
  
  cout << "Case #" << caseNumber << ": " ;
  
  if (isTidy(n))
    cout << n << endl ;
  else {
    ll i ;
    ll l = strlen(n);
    for (i = l-2 ; i >= 0 ; i--) {
      n[i+1] = '9';
      if (n[0] > '0') {
        n[i] -- ;
        if (isTidy(n)) {
          if (n[i] == '0')
            cout << (n+1) << endl ;
          else
            cout << n << endl ;
          break ;
        }
      }
    }
  }
  return 1 ;
}

////////////////////////////////////////////////////////

int main (int argc, const char * argv[])
{
  int testCases ;
  //testxor();
  cin >> testCases ;
  if (argc > 1) {
    if (argv[1][0] == 'v')
      v = 1 ;
  }
  if (v) {
    cerr << "Verbose is on!" << endl ;
    cout << "// Test cases: " << testCases << endl ;
  }
  for (caseNumber=1 ; caseNumber <= testCases ; caseNumber++) {
    //if (caseNumber > 11) v = 1;
    if (v)
      cout << "// Running case #" << caseNumber << endl ;
    int r = runTest();
    if (!r) {
      cerr << "test failed!" << endl ;
    }
  }
  return 0;
}
