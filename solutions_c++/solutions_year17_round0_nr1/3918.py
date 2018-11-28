#include <iostream>
#include<string>
#include<vector>

using namespace std;

//0 unhappy
int nextNeg(string& s, int f, int n){
	//return next negative face from index k included to n excluded
	for (int i = f; i<n; ++i){
		if (s[i]=='-'){
			return i;
		}
	}
	return n; //n meanning no unhappy
}

int flip(string& s, int k, int j){
	//from k from index j
	//suppose j small enough
	//return index of first positive index
	int n = s.size();
	int positive=j+1;
	bool found = false;
	for (int i = j; i<j+k; ++i){
		if (s[i]=='+'){
			s[i]='-';
			if (! found) positive = i;
			found =true;
		}else{
			s[i] = '+';
		}
	}
	if (! found) positive = j+k;
	return positive;
}

int main(){
	int n;
	cin >> n; cin.ignore();
	vector<string> tests =  vector<string>(n);
	vector<int> range = vector<int>(n);
	for (int i = 0; i<n ; ++i){
		cin >> tests[i]; cin >> range[i]; cin.ignore();
	}

	for (int i = 0; i<n ; ++i){
		cout << "Case #"<<i+1<< ": ";
		int c = 0; //number of flips
		int m = 0;
		string& s = tests[i];
		int n = s.size();
		int k = range[i];
		int p=0;
		while(p<n){
			int j = nextNeg(s, p, n ) ;
			if (j>=n){
				// we finished
				break;
			}
			if ( j>n-k){
				//impossible, not large enough to flip the rest
				//cerr << "j = "<< j <<" too small"<<endl;
				c = -1;
				break;
			}else{
				//flip k from j
				p = flip(s, k, j);
				c++;
			}
		}
		if ( c < 0){
			cout << "IMPOSSIBLE" << endl;
		}else{
			cout << c <<endl;
		}
		//verification
		for (char l : s){
			if (l == '-' && c>=0){
				cerr << "fatal error, final string : " << s <<endl;
			}
		}
	}
}
