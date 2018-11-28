#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

int main()
{
    //ifstream fin("A-small-attempt0.in");
	ifstream fin("A-large.in");
	//ofstream fout("A-small-attempt0.out");
	ofstream fout("A-large.out");    
    int T;
    fin >> T;
      
    int N, P;
    int G[101];
    int count[4];
    for (int t = 1 ; t <= T; t++)
    { 
    	fin >> N >> P;
    	
    	for (int i = 0 ; i < 4 ; i++) {
    		count[i] = 0;
		}
    	for (int i = 0 ; i < N ; i++) {
    		fin >> G[i];
    		G[i] = G[i] % P;
    		count[G[i]]++;
		}
		int ans = count[0];
		if (P == 2) {
			ans += (count[1]+P-1) / P;
		} else if (P == 3) {
			int remain;
			if (count[1] > count[2]) {
				ans += count[2];
				remain = count[1]-count[2];
			} else {
				ans += count[1];
				remain = count[2]-count[1];
			}
			ans += (remain+P-1)/P;
			
		} else if (P == 4) {
			int remain;
			if (count[1] > count[3]) {
				ans += count[3];
				remain = count[1]-count[3];
			} else {
				ans += count[1];
				remain = count[3]-count[1];
			}
			ans += (count[2]+1) / 2;
			if (count[2] % 2 != 0) {
				remain -= 2;
			}
			if (remain > 0) {
				ans += (remain + P-1)/P;
			}
		}
    	fout << "Case #" << t << ": " << ans << endl;
	}
}

