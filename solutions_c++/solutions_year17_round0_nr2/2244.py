#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;


string solve(string N){
	int hist[9];
	int current = 0;
	int flip = -1;
	int flip_qty = 0;
	
	for (int i = 0; i < 9; i++)
		hist[i] = 0;
		
	for (int i = 0; i < N.size(); i++){
		if (current <= N[i] - 49)
			current = N[i] - 49;
		else{
			flip_qty = flip > -1 ? flip_qty : hist[current];
			flip = flip > -1 ? flip : current;
			current = 8;
		}
			
		hist[current]++;
	}
	
	if (flip > -1){
		hist[8] += flip_qty - 1;
		hist[flip] -= flip_qty;
		if (flip > 0)
			hist[flip - 1]++;
	}
	
	string result = "";
	for (int i = 0; i < 9; i++)
		result.append(hist[i], 49 + i);
	
	return result;
}


int main() {	
	ifstream input("B-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			string N;
			input >> N;
					
			
			//cout << "Case #" << n << ": " << solve(N) << "\n";
			output << "Case #" << n << ": " << solve(N) << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
