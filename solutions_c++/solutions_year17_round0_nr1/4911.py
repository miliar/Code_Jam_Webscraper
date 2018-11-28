#include<iostream>

using namespace std;

int t, k;
string s;

bool impossible;
int number_of_flips;

void flip(int b, int e){
	for(int i = b; i <= e; i++){
		if(s[i] == '-')
			s[i] = '+';
		else 
			s[i] = '-';
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	
	cin >> t;
	
	for(int i = 1; i <= t; i++){
		cin >> s >> k;
		
		number_of_flips = 0;
		impossible = false;
		
		for(int j = 0; j < (s.size() - k + 1); j++){
			if(s[j] == '-'){
				flip(j, j + k - 1);
				number_of_flips++;
			}
		}
		for(int j = (s.size() - k + 1); j < s.size(); j++){
			if(s[j] == '-'){
				impossible = true;
				break;	
			}
		}
		cout << "Case #"<<i<<": ";	
		if(impossible == true)
			cout << "IMPOSSIBLE\n";
		else
			cout << number_of_flips << "\n";
	}
	
	cout << endl;
	return 0;
}
