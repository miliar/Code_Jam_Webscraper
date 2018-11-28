#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
using namespace std;
  
int main()
{
    ifstream fin("C-small-1-attempt0.in");
    int T;
    fin >> T;
      
    int N, K;
    double U;

    FILE* pfile = fopen("C-small-1-attempt0.out", "w");
    for (int t = 1 ; t <= T; t++)
    {  
    	fin >> N >> K >> U;
    	vector<double> Ps;
    	
    	double P;
    	for (int i = 0 ; i < N ; i++) {
    		fin >> P;
    		Ps.push_back(P);
    	}
    	sort(Ps.begin(), Ps.end());
    	
    	int idx = N-1;
    	while(idx >= 0) {
    		double sum = 0;
    		for (int i = 0 ; i < idx ; i++) {
    			sum += Ps[idx] - Ps[i];
			}
			if (sum < U) break;
			idx--;
		}
    	double sum = 0;
    	for (int i = 0 ; i <= idx ; i++) {
			sum += Ps[i];
		}
		sum += U;
		sum /= (idx+1);
    	double final_prob = 1;
    	for (int i = 0 ; i < N ; i++) {
    		if (i <= idx) final_prob *= sum;
			else final_prob *= Ps[i]; 
		}
    	std::cout << setiosflags(ios::fixed);
		std::cout << std::setprecision(9);
		
		fprintf(pfile,"Case #%d: %.9f\n", t, final_prob);
	}
	fclose(pfile);
}

