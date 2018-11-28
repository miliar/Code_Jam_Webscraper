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

//string CaseName = "pancake";
//string CaseName = "A-small-attempt0";
string CaseName = "A-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;

bool AllHappy(string &pancakes) {
  
  for (auto p : pancakes) {
    if (p == '-') {
      return false;
    }
  }  
  
  return true;
}

void flip(string &pancakes, int count, int K) {
  
  for (int i = count; i < (count+K); i++) {
    pancakes[i] = (pancakes[i] == '+') ? '-' : '+' ;
  }
  return;
}

void Solve(void) {
  
  // Read in the string //
  string pancakes;
  int K;
  In >> pancakes >> K;
  
  int N = pancakes.size();
  
  long flips = 0;
  
  int count = 0;
  //cout << AllHappy(pancakes) << endl;
  while(!AllHappy(pancakes)) {
    //cout << pancakes << " " << K << " " << count << endl;
    if (pancakes[count] != '+') {
      // Flip //
      if (count + K -1 < N) {
        flip(pancakes, count, K);
        flips++;
      } else {
        break;
      }
    
    }
    count++;
    
  }
  
  bool finalcheck = AllHappy(pancakes);
  
  if (finalcheck) {
    Out << flips << endl;
    cout << flips << endl;
  } else {
    Out << "IMPOSSIBLE" << endl;
    cout << "IMPOSSIBLE" << endl;
  }
  
  return;
}

int main() {

	int NCases; 
	
	In.open(CaseName+".in");
	
	// Reads Number of cases //
  In >> NCases;
  
  Out.open(CaseName+".out");
  
	
	int i,j;

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
