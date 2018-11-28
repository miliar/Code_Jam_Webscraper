#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
using namespace std;

string final_ans;
  
bool DFS (int N, int R, int O, int Y, int G, int B, int V, string ans) {
	
	int max_c = max(max(max(max(max(V,R),O),Y),G),B);
	//cout << N << " : " << R << " " << O << " " << Y << " " << G << " " << B << " " << V << " : " << (N+1)/2 << endl;
	//cout << ans << endl;
	if (max_c > (N+1)/2) return false;
	char last = *ans.rbegin();
	if (R == 0 && O == 0 && Y == 0 && G == 0 && B == 0 && V == 0) {
		char start = *ans.begin();
		cout << start << " -- " << last << endl;
		
		if (start == 'R' && last != 'R' && last != 'O' && last != 'V') { 
			final_ans = ans;
		return true;
		}
		if (start == 'O' && last != 'O' && last != 'R' && last != 'Y') { 
			final_ans = ans;
		return true;
		}
		if (start == 'Y' && last != 'Y' && last != 'O' && last != 'G') { 
			final_ans = ans;
		return true;
		}
		if (start == 'G' && last != 'G' && last != 'Y' && last != 'B') { 
			final_ans = ans;
		return true;
		}
		if (start == 'B' && last != 'B' && last != 'G' && last != 'V') { 
			final_ans = ans;
		return true;
		}
		if (start == 'V' && last != 'V' && last != 'R' && last != 'B') {
		final_ans = ans;
		return true;
		}
		return false;
		
	}
	
	if (R > 0 && last != 'R' && last != 'O' && last != 'V') {
		if (DFS(N-1, R-1, O, Y, G, B, V, ans + 'R')) {
			return true;
		}
	}
	if (O > 0 && last != 'O' && last != 'R' && last != 'Y') {
		if (DFS(N-1, R, O-1, Y, G, B, V, ans + 'O')) {
			return true;
		}
	}
	if (Y > 0 && last != 'Y' && last != 'O' && last != 'G') {
		if (DFS(N-1, R, O, Y-1, G, B, V, ans + 'Y')) {
			return true;
		}
	}
	if (G > 0 && last != 'G' && last != 'Y' && last != 'B') {
		if (DFS(N-1, R, O, Y, G-1, B, V, ans + 'G')) {
			return true;
		}
	}
	if (B > 0 && last != 'B' && last != 'G' && last != 'V') {
		if (DFS(N-1, R, O, Y, G, B-1, V, ans + 'B')) {
			return true;
		}
	}
	if (V > 0 && last != 'V' && last != 'R' && last != 'B') {
		if (DFS(N-1, R, O, Y, G, B, V-1, ans + 'V')) {
			return true;
		}
	}
	return false;
}

int main()
{
    ifstream fin("B-small-attempt1.in");
	//ifstream fin("B-large.in");
	ofstream fout("B-small-attempt1.out");
    
    int T;
    fin >> T;
      
    int N, R, O, Y, G, B, V;
    for (int t = 1 ; t <= T; t++)
    { 
    	fin >> N >> R >> O >> Y >> G >> B >> V;
    	
    	fout << "Case #" << t << ": ";
    	
    	
    	bool result = false;
    	if (R > 0) {
    		result = DFS(N-1, R-1, O, Y, G, B, V, "R"); 
		} else if (O > 0) {
			result = DFS(N-1, R, O-1, Y, G, B, V, "O"); 
		} else if (Y > 0) {
			result = DFS(N-1, R, O, Y-1, G, B, V, "Y"); 
		} else if (G > 0) {
			result = DFS(N-1, R, O, Y, G-1, B, V, "G"); 
		} else if (B > 0) {
			result = DFS(N-1, R, O, Y, G, B-1, V, "B"); 
		} else if (V > 0) {
			result = DFS(N-1, R, O, Y, G, B, V-1, "V"); 
		}
    	
    	if (result) {
    		fout << final_ans;
		} else {
			fout << "IMPOSSIBLE";
		}
    	fout << endl;
	}
}

