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
      int N, R, O, Y, G, B, V;
      input >> N >>R>>O>>Y>>G>>B>>V;
      int v[3];
      v[0] = R;
      v[1] = Y;
      v[2] = B;
      int m;
      m = *max_element(v,v+3);
      int w[2];
      char s[3];
      if (m > N/2){
	output << "IMPOSSIBLE\n";
	continue;
      }
      if (v[0] == m){
	    s[0] = 'R';
	    s[1] = 'Y';
	    s[2] = 'B';
	    w[0] = v[1];
	    w[1] = v[2];
      }
      else{
	if (v[1] > v[2]){
	  s[0] = 'Y';
	  s[1] = 'R';
	  s[2] = 'B';
	  w[0] = v[0];
	  w[1] = v[2];
	}
	else{
	  s[0] = 'B';
          s[1] = 'R';
          s[2] = 'Y';
	  w[0] = v[0];
	  w[1] = v[1];
	}
      }
      string ans = "";
      while ( m > 1){
	ans.push_back(s[0]);
	m = m-1;
	if(w[0] > w[1]){
	  ans.push_back(s[1]);
	  w[0] = w[0]-1;
	}
	else{ 
	  ans.push_back(s[2]);
	  w[1] = w[1] -1;
	}
      }
      ans.push_back(s[0]);
      while (w[0] > 0 || w[1] > 0){
	if(w[0] > w[1]){
          ans.push_back(s[1]);
          w[0] = w[0]-1;
	}
        else{
          ans.push_back(s[2]);
          w[1] = w[1] -1;
        }
      }
      output << ans << "\n";
    }
}
