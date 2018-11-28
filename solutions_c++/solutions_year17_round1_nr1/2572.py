#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <set>  
#include <vector>
using namespace std;
  
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
      
    int C, R;
    
    for (int t = 1 ; t <= T; t++)
    {  
    
    	fin >> R >> C;
    	vector<string> row;
    	for (int i = 0 ; i < R ; i++) {
    		string temp;
    		fin >> temp;
    		char now;
    		bool start = true;
    		for (int s = 0 ; s < temp.size() ; s++) {
    			if (temp[s] == '?') {
    				if (!start) {
    					temp[s] = now;	
					}
				} else {
					now = temp[s];
					if (start) {
						for (int ss = 0 ; ss < s ; ss++) {
							temp[ss] = now;
						}
					}
					start = false;
				}
			}
    		row.push_back(temp);
		}
		
		string now;
		bool start = true;
		for (int i = 0 ; i < R ; i++) {
    		if (row[i][0] == '?') {
    			if (!start) {
    				row[i] = now;
				}
			} else {
				now = row[i];
				if (start) {
					for (int ss = 0 ; ss < i ; ss++) {
						row[ss] = now;
					}
				}
				start = false;
			}
		}
        fout << "Case #" << t << ": " << endl;
		for (int i = 0 ; i < R ; i++) {
			fout << row[i] << endl;
		}
	}
}

