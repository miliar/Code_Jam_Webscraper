# include <iostream>
# include <cmath>
# include <vector>
# include <string>
# include <unordered_set>
# include <set>
# include <unordered_map>
# include <map>
# include <algorithm>
# include <ostream>
# include <fstream>
# include <queue>
# include <stack>
# include <climits>

using namespace std;

typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pair<int, int> > vp;
typedef vector<vd> vvd;


# define REP(i,a,b) for(int i = a; i < b; i++)
# define REVREP(i,a,b) for(int i = a; i >= b; i--)
# define newl cout << endl
# define debl(a) cout << a << " "
# define debl2(a,b) cout << a << " " << b << " "
# define debnl(a) cout << a << endl
# define debnl2(a,b) cout << a << " " << b << endl
# define minv(a) *min_element(a.begin(), a.end())
# define maxv(a) *max_element(a.begin(), a.end())
# define minvind(a) min_element(a.begin(), a.end())
# define maxvind(a) max_element(a.begin(), a.end())

//string CaseName = "test";
//string CaseName = "A-small-attempt0";
string CaseName = "A-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;



void Solve(void) {
  
  
  int R, C;
  
  In >> R >> C;
  
  vector<string> cake(R);
  
  REP(i, 0, R) {
    In >> cake[i];
  }
  
  
  vector<string> orig = cake;
  
  REP(i, 0, R) {
    REP(j,0,C) {
      
      if (orig[i][j] != '?') {
        
        //Bleed Row //
        int startk = j, stopk = j;
        for (int k = j+1; k < C; k++) {
          if (cake[i][k] == '?') {
            cake[i][k] = cake[i][j];
            stopk = k;
          } else {
            break;
          }
        }
        
        for (int k = j-1; k >= 0; k--) {
          
          if (cake[i][k] == '?') {
            cake[i][k] = cake[i][j];
            startk = k;
          } else {
            break;
          }
          
        }
        int l;
        // Bleed entire row Up //
        for (int k = i-1; k >= 0; k--) {
          bool cando = true;
          for (l = startk; l <= stopk; l++) {
            if (cake[k][l] != '?') {
              cando = false;
              break;
            }
          }
          
          if (cando) {
            for (l = startk; l <= stopk; l++) {
              cake[k][l] = cake[i][j];
            }
          } else {
            break;
          }
          
        }
        
        // Bleed entire row down //
        for (int k = i+1; k < R; k++) {
          bool cando = true;
          
          for (l = startk; l <= stopk; l++) {
            if (cake[k][l] != '?') {
              cando = false;
              break;
            }
          }
          
          if (cando) {
            for (l = startk; l <= stopk; l++) {
              cake[k][l] = cake[i][j];
            }
          } else {
            break;
          }
        }
      }
            
    }
  }

  REP(i, 0, R) {
    cout << cake[i] << endl;
    Out << cake[i] << endl;
  }

  
  return;
}

int main() {

	int NCases; 
	
	In.open(CaseName+".in");
	
	// Reads Number of cases //
  In >> NCases;
  
  Out.open(CaseName+".out");
  
	
	int i;

  REP(i,1,NCases+1) {
  
		Out << "Case #" << i << ": " << endl;
		cout << "Case #" << i << ": " << endl;		
		
    Solve();
		
	}
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}
