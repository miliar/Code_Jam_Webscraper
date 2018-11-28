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
//string CaseName = "A-small-attempt0";
string CaseName = "A-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;



void Solve(void) {
  
  long D;
  int N;
  
  
  In >> D >> N;
  
//  vector<long> K(N);
//  vi S(N);
  
  vector<pair<long, int> > Pair(N);
  
  REP(i, 0, N) {
    long tmpK, tmpS;
    In >> tmpK >> tmpS;
    Pair[i] = make_pair(tmpK, tmpS);
  }
  
  sort(Pair.begin(), Pair.end());
  
  double speed = 0.0;
  
  vector<double> DestTime(N);
  vector<double> Speed(N);
  
  DestTime[N-1] = (double)(D - Pair[N-1].first)/(double)Pair[N-1].second;
  Speed[N-1] = (double) Pair[N-1].second;
  
  //cout << DestTime[N-1] << endl;
  
  for (int i = N-2; i >= 0; i--) {
    
    double tmp = (double)(D - Pair[i].first)/(double)Pair[i].second;
    
    if (tmp < DestTime[i+1]) {
      
/*      double time1 = (double)(Pair[i+1].first - Pair[i].first)/(double)(Pair[i].second - Pair[i+1].second);
      
      double Dist1 = time1*Pair[i].second;
      
      double time2 = ((double)D - Dist1)/Speed[i+1];
      cout << time1 << " " << time2 << endl; 
      DestTime[i] = time1+time2;
      Speed[i] = (double)(D - Pair[i].first)/DestTime[i]; */
      
      
      Speed[i] = (double)(D - Pair[i].first)/DestTime[i+1];
      DestTime[i] = (double)(D - Pair[i].first)/Speed[i];
      
      
    } else {
      DestTime[i] = tmp;
      Speed[i] = Pair[i].second;
    }
    
//    cout << DestTime[i] << " " << Pair[i].second << endl;
  }
  
  cout << fixed << setprecision(6)  << (double)D/DestTime[0] << endl;
  
  Out << fixed << setprecision(6) << (double)D/DestTime[0] << endl;
  
  
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
