#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

//43 +
//45 -

int solve(string S, int K){
	int flips = 0;
	
	for (int i = 0; i <= S.size() - K; i++)
		if (S[i] == '-'){
			flips++;
			for (int j = 0; j < K; j++)
				S[i + j] = S[i + j] == '+' ? '-' : '+';
		}
	
	
	int ok = 1;
	int i = 0;
	while(i < S.size() && ok == 1){
		if (S[i] == '-')
			ok = 0;
		i++;
	}
	
	return ok == 1 ? flips : -1;
}


int main() {	
	ifstream input("A-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			string S;
			int K;
			input >> S;
			input >> K;
					
			
			int r = solve(S, K);
			if (r > -1)
				cout << "Case #" << n << ": " << r << "\n";
			else
				cout << "Case #" << n << ": " << "IMPOSSIBLE" << "\n";
				
			if (r > -1)
				output  << "Case #" << n << ": " << r << "\n";
			else
				output  << "Case #" << n << ": " << "IMPOSSIBLE" << "\n";
	
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
