#include <iostream>
#include <string>
#include <fstream>

using namespace std;
void result(std::string &);

int main(){
    int T(0), K(0), test(0);
    string S;
    ifstream myfile;
    myfile.open("B-large.in");
    myfile >> T;
    for(int i(0); i < T; ++i){
        myfile >> S;
	cout << "Case #" << i+1 << ": ";
        result(S);
        cout << S << endl;
    }
    myfile.close();
    return 0;
}
void result(std::string &S){
    for(int i(S.size()-1); i > 0; --i){
	if(S[i] < S[i-1]){
	    for(int j(i); j < S.size(); ++j){
		S[j] = '9';
	    }
	    S[i-1] -= 1;
	}
    }
    if(S[0] == '0')
	S.erase(0,1);
}
