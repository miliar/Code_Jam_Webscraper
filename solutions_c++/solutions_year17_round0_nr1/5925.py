#include <iostream>
#include <string>
#include <vector>


using namespace std;

void flip(vector<char>& c, int i, int k){
	for (int j = i; j < i + k; ++j)
	{
		if(c[j] == '+')
			c[j] = '-';
		else
			c[j] = '+';
	}
}

bool check(vector<char>& c, int n){
	int i = 0;
	while(i < n){
		if(c[i++] == '-'){
			return false;
		}
	}
	return true;
}

void print_vector(vector<char> c){
	for (int i = 0; i < c.size(); ++i)
	{
		cout << c[i];
	}
	cout << endl;
}

int main(){
	int T, k;
	string str;
	vector<char> c;
	cin >> T;
	int counter = 0;
	
	
	while(T--){
		cin >> str >> k;
		int n = str.length();
		std::vector<char> c(str.begin(), str.end());
		int f = 0;
		int i = 0;
		while(n - i >= k){
			if(c[i]=='-'){
				
				flip(c, i, k);
				f++;
				
			}
			i++;
		}
		if(check(c, n)){
			cout <<"Case #"<< counter + 1 << ": " << f << endl;
		}
		else{
			cout << "Case #" << counter + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		counter++;

	}
	return 0;
}