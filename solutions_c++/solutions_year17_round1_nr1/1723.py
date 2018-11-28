#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

void print(vector<int> v){
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}

void solve(int R, int C, char t[30][30]){
	cout << R << " " << C << "\n";
	
	for (int i = 0; i < R; i++){
		char last = '?';
		for (int j = 0; j < C; j++){
			if (t[i][j] != '?')
				last = t[i][j];
			else if (last != '?')
					t[i][j] = last;
		}
		
		last = '?';
		for (int j = C - 1; j >= 0; j--){
			if (t[i][j] != '?')
				last = t[i][j];
			else if (last != '?')
					t[i][j] = last;
		}
	}
	
	for (int j = 0; j < C; j++){
		char last = '?';
		for (int i = 0; i < R; i++){
			if (t[i][j] != '?')
				last = t[i][j];
			else if (last != '?')
					t[i][j] = last;
		}
		
		last = '?';
		for (int i = R - 1; i >= 0; i--){
			if (t[i][j] != '?')
				last = t[i][j];
			else if (last != '?')
					t[i][j] = last;
		}
	}
			
}


int main() {	
	ifstream input("A-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			int R, C;
			char t[30][30];
			input >> R >> C;
			for (int i = 0; i < R; i++)
				for (int j = 0; j < C; j++)
					input >> t[i][j];
					
			
			solve(R, C, t);
			
			cout << "Case #" << n << ":\n";
			for (int i = 0; i < R; i++){
				for (int j = 0; j < C; j++)
					cout << t[i][j];
				cout << "\n";
			}
			
			output << "Case #" << n << ":\n";
			for (int i = 0; i < R; i++){
				for (int j = 0; j < C; j++)
					output << t[i][j];
				output << "\n";
			}
			//output << "Case #" << n << ": " << solve(S) << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
