#include<iostream>
#include<string>

using namespace std;

int main(void){
	int total;
	string pencakes;
	int K;
	cin >> total;
	for( int i = 0; i < total ; i++){
	cin >> pencakes;
	cin >> K;
	int count = 0;
	for(int j = 0; j <= pencakes.size()-K; j++){
		if (pencakes[j] == '-'){
			for(int k = 0; k < K; k++){
			pencakes[j+k] = (pencakes[j+k] == '+') ? '-' : '+';
		}
			count++;
		}
	}
	
	cout << "Case #" << i+1 << ": " ;
	if(pencakes.find('-') == string::npos){
		cout << count << endl;
	}
	else{
		cout << "IMPOSSIBLE" << endl;
	}
	}
	return 0;
}