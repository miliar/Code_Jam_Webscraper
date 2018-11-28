#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define PI 3.14159265359

int main(int argc, char ** argv){
    int nTest;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nTest;
    
    outFile.precision(9);
    outFile.setf(ios::fixed, ios::floatfield);

    for(int idx = 0 ; nTest > idx ; idx++){
	double result;
	int n,k;

	vector<double> r;
	vector<double> h;

	vector<double> up;
	vector<double> side;
	vector<double> total;

	r.clear();
	h.clear();
	up.clear();
	side.clear();
	total.clear();

	inFile >> n;
	inFile >> k;

	for(int i= 0 ; n > i ; i++){
	    double t;
	    inFile >> t;
	    r.push_back(t);
	    inFile >> t;
	    h.push_back(t);

	    up.push_back(PI * r.back() * r.back());
	    side.push_back(PI * r.back() * 2 * h.back());
	    total.push_back(up.back() + side.back());
	}
	result = 0.;
	double tu = 0.;

	for(int i= 0 ; k > i ; i++){
	    int idx	= max_element(total.begin(), total.end()) - total.begin();
	    int idx2	= max_element(up.begin(), up.end()) - up.begin();

	    if(tu > up[idx2]){
		idx = max_element(side.begin(), side.end()) - side.begin();
	    }
	    if( tu < up[idx]){
		tu = up[idx];
	    }
	    result  += side[idx];

	    total.erase(total.begin() + idx);
	    up.erase(up.begin() + idx);
	    side.erase(side.begin() + idx);
	}
	result	+= tu;



	outFile << "Case #" << idx+1 <<": " << result << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
