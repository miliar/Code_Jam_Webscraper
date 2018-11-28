#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char *argv[]){
	int N = 0;
	cin >> N;
	for(int I = 1; I <= N; I++){
		string s = "";
		cin >> s;
		int L = s.size();
		int start = 0, i = 0;
		bool X = true;
		while(i < L){
			if((int)s[i] > (int)s[start]){
				start = i;
			}
			else if((int)s[i] < (int)s[start]){
				X = false;
				break;
			}
			i++;
		}
		if(X){cout << "Case #" << I << ": " << s << endl;}
		else{
			string k = "";
			int t = 0;
			if(start == 0 && s[0] == '1'){
				t = L - 1;
			}
			else{
				for(int j = 0; j < start; j++){
					k = k + s[j];
				}
				k = k + (char)((int)s[start] - 1);
				t = L - start - 1;
			}
			for(int j = 0; j < t; j++){
				k = k + "9";
			}
			cout << "Case #" << I << ": " << k << endl;
		}
	}
	return 0;
}