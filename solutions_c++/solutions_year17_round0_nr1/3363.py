#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char ** argv){
    int nTest;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nTest;
    
    string s;
    int k;

    for(int idx = 0 ; nTest > idx ; idx++){
	
	inFile >> s ;
	inFile >> k ;

	int result = 0;

	vector<int> st;

	st.clear();

	for(int i = 0 ; s.size() > i ; i++){
	    if( '+' == s[i])
		st.push_back(0);
	    else
		st.push_back(1);
	}

	int limit = st.size() - k;

	for(int i = 0 ; limit >= i ; i++){
	    if(st[i]){
		result++;
		for(int i2 = 0 ; k > i2 ; i2++){
		    st[i + i2] = (st[i + i2] + 1) % 2;
		}
	    }
	}

	if(st.end() != find(st.begin(), st.end(), 1)){
	    outFile << "Case #" << idx+1 <<": IMPOSSIBLE" << endl;
	    continue;
	}

	outFile << "Case #" << idx+1 <<": " << result << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
