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
  forn (test,tests){
    output << "Case #"<< test+1 << ": ";
    int N, P;
    input >> N >> P;
    int R[N];
    forn (i, N)
      input >> R[i];
    int Q[N][P];
    forn (i, N){
      forn (j, P){
	input >> Q[i][j];
      }
      sort (Q[i], Q[i] + P);
      forn (j,P)
	printf("%d ", Q[i][j]);
      printf("\n");
    }
    int c[N];
    forn (i, N)
      c[i] = 0;
    int ans = 0;
    while (*(max_element(c, c+N)) < P){
      int d[N];
      int e[N];
      forn (i, N){
	d[i] = Q[i][c[i]]*100/90/R[i];
	if (d[i]*R[i]*90/100 > Q[i][c[i]] || Q[i][c[i]] > d[i]*R[i]*110/100)
	  d[i] = 0;
	printf("%d\n", d[i]);
	e[i] = Q[i][c[i]]*100/110/R[i];
	if (Q[i][c[i]]*100 % (110*R[i]) != 0)
	  e[i] = e[i]+1;
	if (e[i]*R[i]*90/100 > Q[i][c[i]]|| Q[i][c[i]] > e[i]*R[i]*110/100)
	  e[i] = 10000000;
	printf("%d\n", e[i]);
      }
      if (*(min_element(d, d+N)) == 0){
	forn(i, N)
	  if (d[i] == 0) c[i] = c[i] +1;
	continue;
      }
      int m = *(max_element(e,e+N));
      printf("%d\n", m);
      int mi = *(min_element(d, d+N));
      printf("%d\n", mi);
      if (mi >= m){
	printf("yahoo\n");
	ans = ans+1;
	forn(i,N)
	  c[i] = c[i] +1;
	continue;
      }
      else{ 
	forn(i, N){
	  if (d[i] < m )
	    c[i] = c[i] +1;
	}
      }
      
      
    }
    output << ans << "\n";
	
  }
}
      
    
