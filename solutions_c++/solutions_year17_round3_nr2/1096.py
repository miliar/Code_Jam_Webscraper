#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	ifstream file("B-small-attempt3.in");
	ofstream out("output.txt");
	int T;
	file >> T;
	for(int t=0; t<T; t++) {
		int a, b;
		file >> a >> b;
		int A1[a], A2[a];
		int B1[b], B2[b];
		for(int i=0; i<a; i++) {
			file >> A1[i] >> A2[i];
		}
		for(int i=0; i<b; i++) {
			file >> B1[i] >> B2[i];
		}

		if(a==2 && ((A2[1]-A1[0]>720 && A2[0]+1440-A1[1]>720) || (A2[0]-A1[1]>720 && A2[1]+1440-A1[0]>720)))
			out << "Case #" << t+1 << ": 4" << endl;
		else if(b==2 && ((B2[1]-B1[0]>720 && B2[0]+1440-B1[1]>720) || (B2[0]-B1[1]>720 && B2[1]+1440-B1[0]>720)))
			out << "Case #" << t+1 << ": 4" << endl;
		else 
			out << "Case #" << t+1 << ": 2" << endl;
 		//cout << "Case #" << t+1 << ": " << endl;	
	}
}