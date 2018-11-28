#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>


using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int main ()
{
  
  ifstream input;
  ofstream output;
  input.open("in.txt");
  output.open("out.txt");
  int test,tests;
  test = 0;
  input >> tests;
  printf("%d\n", tests);
  forn (test,tests)
    {
      printf("%d\n", test);
      printf("%d\n", tests);
      string S;
      input >> S;
      int K;
      input >> K;
      int counter = 0;
      int ans = 0;
      printf("%d\n", ans);
      forn (counter,S.length()-K+1){
	if (S[counter] == '-'){
	  ans = ans+1;
	  forn(counter2, K){
	    if (S[counter2+counter] == '-')
	      S[counter2+counter] = '+';
	    else
	      S[counter2+counter] = '-';
	  }
	}
      }
      bool poss = false;
      forn (counter, K-1){
	if (S[S.length()-counter-1] == '-'){
	  poss = true;
	  break;
	}
      }
      if (poss){
	output << "Case #"<< test+1 << ": " << "IMPOSSIBLE" << "\n";
	continue;
      }
	
       output << "Case #"<< test+1 << ": " << ans << "\n";
      
    }
}

