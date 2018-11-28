#include <bits/stdc++.h>
using namespace std;

bool myfunction (int i,int j) { return (i<j); }

string convertInt2Str(long long number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}


int main() {
 // cin >> noskipws; 
  long int t, N;
  long double timeMax, ans, K, S, D;
 
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
 
  for (int caseNo = 1; caseNo <= t; ++caseNo) {
  	cin >> D;
  	cin >> N;
    timeMax = 0;
    for(int i=0;i<N;++i){
      cin >> K;
      cin >> S;

      if((D-K)/S > timeMax){
        timeMax = (D-K)/S;
      }
    }
    		
  	ans = D/timeMax;

   cout << "Case #" << caseNo << ": " << fixed << setprecision(6) << ans <<endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}
