#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
#include<math.h>

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
  
  forn (test,tests)
    {
      output << "Case #"<< test+1 << ": ";
      long long N;
      long long K;
      input >> N;
      input >> K;
      long long m = K;
      int l = 0;
      while (m != 0){
	m = m/2;
	l = l+1;
      }
      m = 1;
      int counter;
      forn (counter, l-1)
	m = m*2;
      m = m-1;
      
      
      long long ass = N - m;
      long long unass = K - m;
      long long len = ass/(m+1);
      long long frac = ass-len*(m+1);
      if (unass <= frac)
	len = len+1;
      len = len-1;
      long long lans = len/2;
      long long rans = len/2;
      if (lans+rans != len)
	rans = rans+1;
      output << rans << " " << lans << "\n";
    }
}
