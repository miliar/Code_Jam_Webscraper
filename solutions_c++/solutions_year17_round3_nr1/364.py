#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
using namespace std;
  
const double pi = std::acos(-1);

int main()
{
    ifstream fin("A-large.in");
    int T;
    fin >> T;
      
    int N, K;
    
    
    FILE* pfile = fopen("A-large.out", "w");
    for (int t = 1 ; t <= T; t++)
    {  
    	fin >> N >> K;
    	vector<double> areas;
    	
    	int R, H;
    	double final_area = 0;
    	
    	vector<int> Rs;
    	vector<int> Hs;
    	for (int i = 0 ; i < N ; i++) {
    		fin >> R >> H;
    		Rs.push_back(R);
    		Hs.push_back(H);
    	}
    	
    	int max_r = 0;
    	for (int i = 0 ; i < K ; i++) {
    		int idx = 0;
    		double max_area = 0;
    		double temp = 0;
    		for (int j = 0 ; j < Rs.size() ; j++) {
    			temp = 2*(double)Rs[j]*(double)Hs[j];
    			if (Rs[j] > max_r) {
    				temp += (double)Rs[j]*(double)Rs[j]-(double)max_r*(double)max_r;
				}
    			temp *= pi;
    			if (temp > max_area) {
    				max_area = temp;
    				idx = j;
				}
			}
			cout << K << " : " << idx << " -- " << max_area << endl;
			if (max_r < Rs[idx]) {
				max_r = Rs[idx];
			}
			Rs.erase(Rs.begin() + idx);
			Hs.erase(Hs.begin() + idx);
			final_area += max_area;
		}
    	
    	std::cout << setiosflags(ios::fixed);
		std::cout << std::setprecision(9);
		
		fprintf(pfile,"Case #%d: %.9f\n", t, final_area);
	}
	fclose(pfile);
}

