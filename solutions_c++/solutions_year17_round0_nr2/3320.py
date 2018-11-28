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

    for(int idx = 0 ; nTest > idx ; idx++){
	inFile >> s;

	bool flag;

	int limit   = s.size() -1;



	do{
	    flag    = false;
	    for(int i = 0 ; limit > i ; i++){
		if(flag){
		    s[i+1] = 57;
		}else if(s[i] > s[i+1]){
		    flag = true;
		    s[i] = s[i] -1;
		    s[i+1] = 57;
		}
	    }
	}while(flag);

	int result = atoi(s.c_str());

	outFile << "Case #" << idx+1 <<": " << result << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
