#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	ifstream file("A-large.in");
	ofstream out("output.txt");
	int T;
	string str;
	file >> T;
	for(int t=0; t<T; t++) {	
		double d;
		int h;
		file >> d >> h;
		double ans = 10000000000000000;
		for(int i=0; i<h; i++) {
			double a, b;
			file >> a >> b;
			double temp = (d-a) / b;
			temp = d/temp;
			if(ans > temp) ans = temp; 
		}
		out << "Case #" << t+1 << ": " << fixed << setprecision(6) <<ans << endl;		
	}
}