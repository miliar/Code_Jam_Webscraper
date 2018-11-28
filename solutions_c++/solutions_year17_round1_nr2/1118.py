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
string CaseName = "B-small-attempt0";
//string CaseName = "B-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;

vvi AllComb;

void comb(vvi &Q, int i, vi ac) {

  if (i == Q.size()) {
    AllComb.push_back(ac);
  } else {
    vi r = Q[i];
    REP(j, 0, r.size()) {
      vi tmp(ac);
      tmp.push_back(r[j]);
      comb(Q, i+1, tmp);
    }
  }

}


void Solve(void) {
  
  //cout << endl;
  int N, P;
  In >> N >> P;
  
  vector<int> R(N);
  
  REP(i, 0, N) {
    In >> R[i];
  }
  
  vvi Q(N, vi(P,0));

  vector<map<int, int>> used(N);

  REP(i, 0, N) {
    REP(j, 0, P) {
      In >> Q[i][j];
      
      if (used[i].find(Q[i][j]) == used[i].end()) {
        used[i][Q[i][j]] = 1;
      } else {
        used[i][Q[i][j]]++;
      }
      
      
    }
  }
  
  
  int m = *max_element(R.begin(), R.end());
  int MaxServing = 1000000/m;
  
  //cout << MaxServing << endl;
  

  

  
  
  vi ac;  
  comb(Q, 0, ac);
  
  int Npack = 0;
  
  for (int i = 0; i < AllComb.size(); ++i) {
    
    vi Ratio(AllComb[i].size(), 0);
    
    bool found = false;
    
    for (int ser = 1; ser <= MaxServing; ser++) {
      
      bool possi = true;
      
      for (int j = 0; j < AllComb[i].size(); j++) {
        //cout << AllComb[i][j] << " ";
        
           
        
        double req = (double)(R[j]*ser);
        double low = (double)req*0.9;
        double high = (double)req*1.1;
        
        if (used[j][AllComb[i][j]] == 0) {
          possi = false;
          break;
        }
        
        if ((AllComb[i][j] <= high) && (AllComb[i][j] >= low)) {
          // Possible //
          //cout << ser << endl;
        } else {
          possi = false;
          break;
        }
        
     /*
        double rat = (double)AllComb[i][j]/(double)R[j];
        
        
        double ratlower = rat/0.9;
        double ratupper = rat/1.1;
        
        if (ratlower >= ceil(rat)) {
          Ratio[j] = (int) ceil(rat);
        } else if (ratupper <= floor(rat)) {
          Ratio[j] = (int) floor(rat);
        }
        
        cout << ratlower << " ";
        
        //cout << Ratio[j] << " ";
        */
       
      }
      
      if (possi) {
        found = true;
        
        for (int ll = 0; ll < AllComb[i].size(); ll++) {
          used[ll][AllComb[i][ll]]--;
        }
        
        break;
      }
      
      //cout << endl;
    
    }
    
    if (found) {
      Npack++;
    }
    
  }
  
  cout << Npack << endl;
  Out << Npack << endl;
  
  AllComb.clear();

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
  
		Out << "Case #" << i << ": ";
		cout << "Case #" << i << ": ";		
		
    Solve();
		
	}
	// Close Input and Output Files //
	In.close();
	Out.close();

	return 0;

}
