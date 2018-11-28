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
      output << "Case #"<< test+1 << ": ";
      int R,C;
      input >> R >> C;
      string S[R];
      forn (i, R){
	input >> S[i];
	printf("%s\n",S[i].c_str());
      }
      int start = 0;
      int rep = 0;
      forn (start, R){
	printf("%d\n", start);
	forn (j, C){
	if (S[start][j]!='?'){
	  printf("%d\n", start);
	  char temp = '?';
	  forn (i, C)
	    if (S[start][i] != temp){
	      temp = S[start][i];
	      break;
	    }
	  forn (i, C){
	    if (S[start][i] == '?')
	      S[start][i] = temp;
	    else 
	      temp = S[start][i];
	  }
	  forn (i, start){
	    forn (j, C){
	      S[start-i-1][j] = S[start][j];
	    }
	  }
	  rep = 1;
	  break;
	  
	}
	}
	printf("%d\n", rep);
	if (rep == 1) break;
      }
      forn (i, R-1){
	char temp = '?';
	forn (j, C){
	  if (S[i+1][j] != temp){
	    temp = S[i+1][j];
	    break;
	  }
	}
	  
	forn (j, C){
	  if (S[i+1][j] == '?'){
	    if (temp == '?')
	      S[i+1][j] = S[i][j];
	    else
	      S[i+1][j] = temp;
	  }
	  else
	    temp = S[i+1][j];
	}
      }
      output << "\n";
      forn (i, R){
	output << S[i] << "\n";
      }
    }
}
    
	      
	      
	  
	  
