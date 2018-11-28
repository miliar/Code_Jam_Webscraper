#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;

vector<int> solve(string N);

int main(int argc, char **argv){

	ifstream input(argv[1], ios::in);
	ofstream output;
	output.open("output", ios::out);	
	
	int T; input >> T;
	for (int i = 0; i<T; i++){
		string N;
		input >> N;
		output <<"Case #"<<i+1<<": ";
		vector<int> returnedValue = solve(N);
		for (auto j: returnedValue)
		output<<j;
		output<<endl;

	}
	
	input.close();
	output.close();
}



vector<int> solve(string N){
	int m = N.size();
	vector<int> aux(m);
	for (int i = 0; i<m; i++) aux[i] = N[i]-'0';


	for (int i = m-1; i>0; i--){
		if (aux[i] < aux[i-1]){
			aux[i-1]--;
			for (int j =i; j<m; j++) aux[j] = 9; 
		}
		
	}
	auto it = aux.begin();
	while(*it == 0){
		aux.erase(it);
	}


	return aux;
}
