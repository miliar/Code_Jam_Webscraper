#include <fstream>
#include <string>
#include <stdlib.h> 

using namespace std;

int main(){
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	int cases;
	infile >> cases;
	for (int t = 0; t < cases; t++){
		string flip;
		int n;
		infile >> flip >>n;
		int count = 0;
		int len = flip.length();
		for (int i = len - 1; i >= n-1; i--){
			if (flip[i] == '-'){
				int k = 0;
				count++;
				while (k <= n-1){
					if (flip[i - k] == '-'){
						flip[i - k] = '+';
					}
					else
					{
						flip[i - k] = '-';
					}
					k++;
				}
			}
		}
		bool ok = true;
		for (int i = 0; i < n-1; i++){
			if (flip[i] == '-'){
				outfile << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
				ok = false;
				break;
			}
		}
		if (ok){
			outfile << "Case #" << t + 1 << ": " << count << endl;
		}
	}
	return 0;
}