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
      output << "Case #"<< test+1 << ": ";
      int N, K;
      input >> N >> K;
      double U;
      input >> U;
      double P[N];
      forn(i, N)
	input >> P[i];
      sort(P, P+N);
      
     
      
	
      int curr = 1;

      while(U > 0.0 && curr < N){
	if (U > (double)curr*(P[curr] - P[curr-1])){
	  U = U- (double)curr*(P[curr] -P[curr-1]);
	  forn(i, curr)
	    P[i] = P[curr];
	}
	else{
	  
	  forn(i, curr)
	    P[i] = P[i] + (double)U/curr;
	  U = 0.0;
	  //printf("%.9f\n", P[curr-1]);
	  //printf("yahoo\n");
	}
	curr = curr+1;
	//printf("%.9f\n", P[curr-1]);
      }
      if (U > 0.0)
	forn (i, N)
	  P[i] = P[i] + (double)U/N;
      //printf("%.9f\n", P[curr-1]);
      double ans = 1.0;
      forn(i, N)
	ans = ans*(P[i]);
      printf("Case #");
      printf("%d", test+1);
      printf(": ");
      //output << "Case #"<< test+1 << ": ";
      printf("%.9f\n", ans);
    }
}
      
