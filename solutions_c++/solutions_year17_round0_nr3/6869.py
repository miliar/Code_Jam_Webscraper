#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>  
using namespace std;
  
int main()
{
    ifstream fin("C-small-1-attempt0.in");
    ofstream fout("C-small-1-attempt0.out");
    int T;
    fin >> T;
      
    long long N, K;
    for (int t = 1 ; t <= T; t++)
    {  
        fin >> N >> K;
        bool stalls [1100];
        for (int i = 0 ; i <= N+1 ; i++) {
        	stalls[i] = false;
		}
        stalls[0] = true;
        stalls[N+1] = true;
        int min_y, max_y;
        for (int i = 1; i <= K ; i++) {
        	min_y = 0;
        	max_y = 0;
        	int Ls = 0;
        	int Rs = 0;
        	int chosen = 0;
        	for (int s = 0 ; s <= N+1 ; s++) {
        		if (stalls[s]) continue;
        		for (int f = s; f >= 0 ; f--) {
        			if (stalls[f]) {
        				Ls = s-f-1;
						break;	
					} 
				}
				for (int f = s; f <= N+1 ; f++) {
        			if (stalls[f]) {
        				Rs = f-s-1;
						break;	
					} 
				}
				if (min(Ls,Rs) > min_y) {
					min_y = min(Ls,Rs);
					max_y = max(Ls,Rs);
					chosen = s;
				} else if (min(Ls,Rs) == min_y) {
					if (max(Ls,Rs) > max_y) {
						max_y = max(Ls,Rs);
						chosen = s;
					}
				}
			}
			stalls[chosen] = true;
		}

		fout << "Case #" << t << ": " << max_y << " " << min_y << endl;
	}
}

