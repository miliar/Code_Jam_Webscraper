#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char ** argv){
    int nTest;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    outFile.precision(6);
    outFile.setf(ios::fixed, ios::floatfield);

    inFile >> nTest;
    
    for(int idx = 0 ; nTest > idx ; idx++){

	int D, N;
	int K, S;

	double time = 0.;
	double temp = 0.;

	inFile >> D;
	inFile >> N;


	for(int i = 0 ; N > i ; i++){
	    inFile >> K;
	    inFile >> S;

	    temp	= static_cast<double>(D - K) / S;

	    if(time < temp){
		time	= temp;
	    }
	}

	outFile << "Case #" << idx+1 <<": " << D / time << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
