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
  //printf("%d\n", tests);
  forn (test,tests)
    {
      printf("Case #");
      printf("%d", test+1);
      printf(": ");
      output << "Case #"<< test+1 << ": ";
      double D;
      int N;
      input >> D >> N;
      //printf("%f\n", D);
      double K[N];
      double S[N];
      forn (i,N)
	input >> K[i] >> S[i];
      double d = 0.0;
      forn (i,N)
	if ((D-K[i])/S[i] > d)
	  d = (D-K[i])/S[i];
      double ans = D/d;
      printf("%.9f", ans);
      printf("\n");
      //output << fixed << std::setprecision(15) <<ans << "\n";
    }
}
		      
