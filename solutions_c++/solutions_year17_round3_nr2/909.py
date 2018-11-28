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
  //#printf("%d\n", tests);
  forn (test,tests)
    {
      output << "Case #"<< test+1 << ": ";
      int C, J;
      input >> C >> J;
      if (C+J <= 1 ){
	input >> C >> J;
	output << "2" << "\n";
	continue;
      }
      if (C == 1 & J==1){
	input >> C >> J;
	input >> C >> J;
	output << "2" << "\n";
	continue;
      } 
      int c[2], d[2];
      forn(i, 2)
	input >> c[i] >> d[i];
      sort(c, c+2);
      sort(d, d+2);
      if ( d[1] - c[0] <= 720 || d[0]+1440 - c[1] <= 720){
	output << "2" << "\n";
	continue;
      }
      output << "4" << "\n";
      //continue;
    }
}
