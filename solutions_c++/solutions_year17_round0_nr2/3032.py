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
      string N;
      input >> N;
      int counter = 0;
      output << "Case #"<< test+1 << ": ";
      int size = N.length();
      if (size == 1){
	output << N <<"\n";
	continue;
      }
      forn (counter, size-2){
	if(N[size-counter-2] > N[size-counter-1]){
	  int counter2;
	  forn (counter2, counter+1){
	    N[size-counter2-1] = '9';
	  }
	  if (N[size-counter-2] == '0'){
	    int temp = size-counter-2;
	    while (N[temp] == '0'){
	      N[temp] = '9';
	      temp--;
	    }
	    N[temp]--;
	  }
	  else 
	    N[size-counter-2]--;
	}
      }
      
      if (N[0] > N[1]){
	if (N[0] == '1'){
	  printf("hello\n");
	  forn (counter2, size-1)
	    output << "9";
	  output << "\n";
	  continue;
	}
	N[0]--;
	output << N[0];
	forn (counter2, size-1)
	  output << "9";
	output << "\n";
	continue;
      }
      if (N[0] == '0'){
	printf("hello\n");
	forn (counter2, size-1)
	  output << "9";
	output << "\n";
	continue;
      }
      output << N << "\n";
    }
}
	
      
