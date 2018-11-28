#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>  
using namespace std;
  
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T;
    fin >> T;
      
    long long S;
    for (int t = 1 ; t <= T; t++)
    {  
        fin >> S;
	std::vector<int> digit;
	while (S > 0) {
	  int temp = S % 10;
	  S /= 10;
	  digit.push_back(temp);
	}
	
	for (int i = 0 ; i < digit.size() ; i++)
	  cout << digit[i] << " ";
        cout << endl;

	for (int i = 0 ; i < digit.size()-1 ; i++) {
		if (digit[i] < digit[i+1]) {
			for (int ii = 0 ; ii <= i ; ii++) 
				digit[ii] = 9;
			int j = i+1;
			while (j < digit.size()) {
				if (digit[j] == 0) {
					digit[j] = 9;
					j++;
				} else {
					digit[j] -= 1;
					break;
				}	
			}
		}
	}
	
	fout << "Case #" << t << ": ";
	bool first_zero = false;
	for (int i = digit.size()-1 ; i >= 0 ; i--) {
		if (!first_zero) {
			if (digit[i] != 0) {
				first_zero = true;
			} else {
				continue;
			}
		}
		fout << digit[i];
	}
        fout << endl;
    }
}

