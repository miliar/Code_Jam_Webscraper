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
  //printf("%d\n", tests);
  forn (test,tests)
    {
      output << "Case #"<< test+1 << ": ";
      int N,K;
      input >> N >> K;
      long long R[N];
      long long H[N];
      long long m[N];
      forn(i, N){
	input >> R[i] >> H[i];
	m[i] = R[i]*H[i];
      }
      long long ans = 0;
      long long temp[N-1];
      forn(i, N){
	long long teans = 0;
	forn(j, N-1)
	  temp[j] = 0;
	int te = 0;
	forn(j, N){
	  if (i !=j){
	    if (R[j] <= R[i]){
	      temp[te] = m[j];
	      te = te+1;
	    }
	  }
	}
	  if (te >= K-1){
	    sort(temp, temp + N-1);
	    forn(j, K-1)
	      teans = teans + temp[N-1-j-1];
	    //printf("%llu\n", teans);
	    teans = teans + m[i];
	    //printf("%llu\n", teans);
	    teans = 2*teans;
	    teans = teans + R[i]*R[i];
	    //printf("%llu\n", teans);
	    //printf("%llu\n", teans);
	  }
	  if (ans < teans)
	    ans = teans;
	
      }
      double rans = (double)ans*M_PI;
      printf("Case #");
      printf("%d", test+1);
      printf(": ");
      //output << "Case #"<< test+1 << ": ";
      printf("%.9f\n",rans);
    }
}
