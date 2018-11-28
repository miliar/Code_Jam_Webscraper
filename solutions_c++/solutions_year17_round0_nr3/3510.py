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
string CaseName = "C-small-2-attempt0";
//string CaseName = "C-large";

// Input Stream for input data //
ifstream In;

// Opens output stream //
ofstream Out;


unsigned long long power(unsigned long long a, int b) {
  
  unsigned long long p = 1.0;
  
  for (int i = 1; i <=b; i++) {
    p = p*a;
  }
  
  return p;
}


void Solve(void) {
  
  unsigned long long N;
  unsigned long long K;
  In >> N >> K;
  
  priority_queue<unsigned long long> pq;
  
  pq.push(N);
  
  while(!pq.empty()) {
  
    // Get the Top Element //
    unsigned long long top = pq.top();
    pq.pop();
    
    if (K == 1) {
      
      if ((top-1)%2 == 0) {
        cout << (top-1)/2 << " " << (top-1)/2 << endl;
        Out << (top-1)/2 << " " << (top-1)/2 << endl;
      } else {
        cout << (top-1)/2 + 1 << " " << (top-1)/2 << endl;
        Out << (top-1)/2 + 1 << " " << (top-1)/2 << endl;
      }
      
      break; 
    } else {
    
      // Split top //
      if ((top-1)%2 == 0) {
        pq.push((top-1)/2);
        pq.push((top-1)/2);
      } else {
        pq.push((top-1)/2 + 1);
        pq.push((top-1)/2);
      }
      
      K--;     
    
    }
    
    
  
  }
  
  

  return;
}


/*
void Solve(void) {

  unsigned long long N;
  unsigned long long K;
  
  In >> N >> K;
  
  int NlevN = 0, NlevK = 0; 
  
  unsigned long long tmp = N;
  while (tmp > 0) {
    NlevN++;
    tmp/=2;
  }
  tmp = K;
  while(tmp > 0) {
    NlevK++;
    tmp/=2;
  }
  
  unsigned long long rem = N/(power(2,NlevK-1));
  
  if ((rem-1)%2 == 0) {
    cout << (rem-1)/2 << " " << (rem-1)/2 << endl;
    Out << (rem-1)/2 << " " << (rem-1)/2 << endl;
  } else {
    cout << (rem-1)/2 + 1 << " " << (rem -1)/2 << endl;
    Out << (rem-1)/2 + 1 << " " << (rem -1)/2 << endl;
  }
  
  cout << NlevN << " " << NlevK << " " << rem << endl;

  return;
}
*/

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
