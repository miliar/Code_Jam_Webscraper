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

// If k = 2^n - 1, then they will be evenly distributed with (n-k)/(k+1) separating, on average
// Next person will go in slot of size ceiling((n-k)/(k+1))
//

int runTest() {
  ll n ;
  ll k ;
  cin >> n ;
  cin >> k ;
  
  cout << "Case #" << caseNumber << ": " ;
  ll i ;
  for (i = 1 ; i*2 <= k ; i*=2) {
  }
  if (v)
    cout << endl << "n k: " << n << " " << k << endl << "i = " << i << endl ;
  
  
  ll j = i-1;
  ll slotSize = (n-j)/(j+1);
  if ((k-j) <= ((n-j) % (j+1)) )
    slotSize ++ ;
  
  cout << (slotSize)/2 << " " << (slotSize-1)/2 << endl ;
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
