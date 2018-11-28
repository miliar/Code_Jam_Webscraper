#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int result(std::string &, int);
bool smiling(std::string &);

int main(){
    int T(0), K(0), test(0);
    string S;
    ifstream myfile;
    myfile.open("A-large.in");
    myfile >> T;
    for(int i(0); i < T; ++i){
        myfile >> S >> K;
        cout << "Case #" << i+1 << ": ";
        test = result(S, K);
	if(test == -1)
	    cout << "IMPOSSIBLE" << endl;
	else
	    cout << test << endl;
    }
    myfile.close();
    return 0;
}

int result(std::string &S, int K){
    int count(0);
    if(smiling(S))
        return count;
    for(int i(0); i <= S.size()-K; ++i){
        if(S[i] == '-'){
            count++;
	    for(int j(0); j < K; ++j){
		if(S[i+j] == '-')
		    S[i+j] = '+';
		else
		    S[i+j] = '-';
	    }
	    if(smiling(S))
                return count;
	}
    }   
    return -1;
}
bool smiling(std::string &S){
    for(int i(0); i < S.size(); ++i){
        if(S[i] == '-')
	    return false;
    }
    return true;
}
