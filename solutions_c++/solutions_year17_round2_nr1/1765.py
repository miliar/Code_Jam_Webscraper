#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
using namespace std;
  
int main()
{
    //ifstream fin("A-small-attempt0.in");
    ifstream fin("A-large.in");
    int T;
    fin >> T;
      
    long long D, N;
    FILE* pfile = fopen("A-large.out", "w");
    for (int t = 1 ; t <= T; t++)
    {  
    	fin >> D >> N;
    
    	double longest_time = 0;
    	for (int i = 0 ; i < N ; i++) {
    		long long temp_K;
    		int temp_S;
    		fin >> temp_K >> temp_S;
    		double timing = (double)(D-temp_K) / (double)temp_S;
    		if (longest_time < timing) {
    			longest_time = timing;
			}
		}
    	
    	std::cout << setiosflags(ios::fixed);
		std::cout << std::setprecision(6);
		
		fprintf(pfile,"Case #%d: %.6f\n", t, D / longest_time);
	}
	fclose(pfile);
}

