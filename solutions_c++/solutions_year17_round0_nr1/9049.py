#include <iostream>
#include <string>

using namespace std;

void flip(string& cake, int start, int length){
	if ( start+length-1 >= cake.length() ){	
		return;
	}
	for (int i=start; i<start+length+1; i++)
		cake[i] = ( cake[i] == '+' )? '-' : '+';
}

bool done(string cake){
	return ( cake.find('-') == -1 );
}



string test(string cake, int length){
	string rep;
	int i=0, j=0;
	for (; i<cake.length();i++ ){
		if ( cake[i] == '+'  ) {
			continue;
		}
		else if ((i + length-1) < cake.length() ){
			flip(cake, i-1, length);
			j++;
		}
		else {
			return "IMPOSSIBLE";	
		}
	}
	return  std::to_string(j);	
}



int main (int argc, char* argv[]) {
	int i;
	cin >> i;
	string cakes[i];
	int sizes[i];
	for (int j=0; j<i; j++){
		cin >> cakes[j] >> sizes[j];
		cout << "Case #" << j+1 << ": "<< test(cakes[j], sizes[j]) << endl;
	}
	return 0;
}
