# include <iostream>
# include <cmath>
# include <vector>
# include <string>
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

//string CaseName = "prac";
//string CaseName = "B-small-attempt0";
string CaseName = "B-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;

void Digitize(vector<int> &dig, unsigned long long N) {
  
  int count = 0;
  
  while((count < 20) && N > 0) {
    
    dig[count] = N%10;
    N /= 10;
    count++;
  }
  
  return;
}

bool CheckSorting(vector<int> &dig) {
  
  for (int i = 0; i < dig.size()-1; ++i) {
    if (dig[i] < dig[i+1]) return false;
  }
  
  return true;
}



void Solve(void) {

  unsigned long long N;
  
  In >> N;
  
  // Digitize into a vector //
  vector<int> dig(20, 0);
  
  Digitize(dig, N);
  
  int count = 0;
  
  while((!CheckSorting(dig)) && (count < 20)) {
    
    dig[count] = 9;
    dig[count+1]--;
    count++;
  }
  
  // Print dig //
  bool start = false;
  for (int i = dig.size()-1; i >= 0; i--) {
    if (dig[i] > 0) {
      start = true;
    }
    
    if (start) {
      cout << dig[i];
      Out << dig[i];
    }
  }
  cout << endl;
  Out << endl;

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
