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
# include <iomanip>

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
string CaseName = "C-small-1-attempt1";
//string CaseName = "C-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;



void SolveS1(void) {
  
  int N, K;
  double MINRES = 1e-4;
  
  In >> N >> K;
  
  double avail;
  In >> avail;
  
  vector<double> P(N);
  double need = 0.0;
  
  for (int i = 0; i < N; ++i) {
    In >> P[i];
    need += (1 - P[i]);
  }
  
  double FinalProb = 1.0;

  if (need <= avail) {
    cout << fixed << setprecision(6) << FinalProb << endl;
    Out << fixed << setprecision(6) << FinalProb << endl;
    return;
  }
  
  
  // Sort the P //
  sort(P.begin(), P.end());
  
  while (avail > 0.0) {
    
    // Add avail to the begin core //
    double ne = P[1] - P[0] + MINRES;
    
    if (ne <= avail) {
      P[0] += ne;
      avail -= ne;
    } else {
      P[0] += avail;
      avail = 0.0;
      break;
    }
    
    // Swap the first two //
    /*if (P[0] > P[1]) {
      swap(P[0], P[1]);
    } else {
      break;
    }*/
    
    sort(P.begin(), P.end());
    
  }
  
  
  for (int i = 0; i < K; ++i) {
    FinalProb*= P[i];
  }
  
  cout << fixed << setprecision(6) << FinalProb << endl;
  Out << fixed << setprecision(6) << FinalProb << endl;
  
  
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
  
		Out << "Case #" << i << ": " ;
		cout << "Case #" << i << ": ";		
		
    SolveS1();
		
	}
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}
