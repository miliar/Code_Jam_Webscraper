/*
ID: georgeh10
PROG: cake
LANG: C++11                 
*/

#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i=0; i<(n); i++)
#define debug(x) cout << '>' << #x << ":" << x << "\n";

const int INF = 1<<29;

int main() {
  ofstream fout ("test.out");
  ifstream fin ("test.in");

  int n, r, c;
  string row;

  fin >> n;
  rep(i,n) {
  	fin >> r >> c;
    string last_row = "";
    int counter = 1;
  	fout << "Case #" << i+1 << ":\n";
  	rep (x,r) {
  		bool empty = true;
  		fin >> row;
  		rep (y,c) {
  			if (row[y] != '?') {
  				empty = false;
  			}
  		}

  		if (empty) {
  			if (last_row != "") {
  				rep(z, counter) {
						fout << last_row << "\n";
  				}	
  				counter = 1;
  			}
  			else {
  				counter += 1;
  			}
  		}

  		else {
  			char last = ' ';
  			int cCount = 1;
  			string result = "";
  			rep (k,c) {
  				if (row[k] != '?') {
  					last = row[k];
  					if (cCount > 1) {
  						rep(banana, cCount-1) {
								result += last;
	  					}	
	  					cCount = 1;
  					}
  					result += row[k];
  				}
  				else {
  					if (last != ' ') {
	  					rep(banana, cCount) {
								result += last;
	  					}	
	  					cCount = 1;
  					}
	  				else {
	  					cCount += 1;
	  				}
  				}
  			}
  			last_row = result;
        if (counter > 1) {
          rep(z, counter-1) {
            fout << last_row << "\n";
          } 
          counter = 1;
        }
  			fout << result << "\n";
  		}
  	}
  }
  return 0;
}
