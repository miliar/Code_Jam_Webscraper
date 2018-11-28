// string::begin/end
#include <iostream>
#include <string>
#include <iterator>
#include <cstring>
#include <fstream>
#include <sstream>
#include <boost/lexical_cast.hpp>
using namespace std;

string tidy(string &num_str) {
	// cout << "Doing for " <<  num_str << endl;
	if(num_str.length() == 1) {
		return num_str;
	}
	string curr;
	curr = num_str;
	string::const_iterator it;

	while( 1 )  {
		// cout << "Check: " << curr << endl;
		int i;
		for (i=0; i<curr.length()-1; i++) {
			// cout << "Comparing " << curr[i]- '0' << " and " << curr[i+1] -'0'  << endl;
			if(curr[i+1] -'0' < curr[i]- '0') {
				break;
			}
		}
		if( i  == curr.length()-1 ) {
			// cout << "found " << i <<endl;
			return curr;
		}
		// Skip this number, decrement and continue search
		// curr = boost::lexical_cast<int>(atoi(curr.c_str())-1);
		curr = boost::lexical_cast<string>(atoi(curr.c_str())-1);
	}

	// 	for( it = curr.begin(); it!=curr.end()-1; it++ ) {
	// 		cout << "Comparing " << *it << " and " << *(it+1)  << endl;
	// 		if (*(it+1) >= *it) {
	// 			cout << "Yeees"<<endl;
	// 			continue;
	// 		}
	// 		else {
	// 			break;	
	// 		}
	// 	}

	// 	if( it == curr.end()-1) {
	// 		// FOUND
	// 		cout << "found " << *it<<endl;
	// 		return curr;
	// 	}
	// 	// Skip this number, decrement and continue search
	// 	curr = atoi(curr.c_str())-1;

	// }
}

int main(int argc, char** argv){
	string filename;
	fstream inputfile;
	ofstream input;
	string S;
	ifstream infile;
	infile.open(argv[1]);
	int counter = 0;
	string casenb = "Case #";
    string n_cases, num_str;
    infile>>n_cases;
    for( int i=0; i<atoi(n_cases.c_str()); i++ ) {	
        infile>>num_str;
        cout << "Case #" << i+1 << ": " << tidy(num_str) << endl;
    }
	// output.close();
	// system ("pause");
	// string S = "1256";
	// string S2 = "99999999999999999";
	// bool y = is_tidy(S2);
	// cout << " y = " << y<<endl;
	return 0;

}