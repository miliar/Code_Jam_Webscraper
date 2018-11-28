#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
  int T;
  cin >> T;

  for(int t = 0; t < T; ++t) 
  {
      string N;
      cin >> N;

      for(int i = N.length()-1; i >= 1; --i) {
            
            if(N[i-1] > N[i]) {

                N[i-1]--;

                for(int j = i; j < N.length(); ++j) {
                    N[j] = '9';
                }

            }
      }

      cout << "CASE #" << t+1 << ": " << strtol(N.c_str(),NULL,10) << '\n';
  }

  return 0;
}