#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	ifstream file("B-small-attempt2.in");
	ofstream out("output.txt");
	int T;
	string str;
	file >> T;
	for(int t=0; t<T; t++) {	
		int N, R, O, Y, G, B, V;
		file >> N >> R >> O >> Y >> G >> B >> V;	
		char last = 'N';
		string str;
		while(N>0) {
			N--;
			if(last == 'R') {
				if(Y >= B) {
					last = 'Y';
					str += string(1,last);
					Y--;
				}
				else {
					last = 'B';
					str += string(1,last);
					B--;
				}
			}
			else if(last == 'Y') {
				if(B >= R) {
					last = 'B';
					str += string(1,last);
					B--;
				}
				else {
					last = 'R';
					str += string(1,last);
					R--;
				}
			}	
			else if(last == 'B') {
				if(R >= Y) {
					last = 'R';
					str += string(1,last);
					R--;
				}
				else {
					last = 'Y';
					str += string(1,last);
					Y--;
				}
			}	
			else {
				if(R <= Y && R <= B && R>0) {
					last = 'R';
					str += string(1,last);
					R--;					
				}
				else if (Y <= R && Y <= B && Y>0) {
					last = 'Y';
					str += string(1,last);
					Y--;					
				}
				else {
					last = 'B';
					str += string(1,last);
					B--;
				}
			}
		}
		if(R==0 && O==0 && Y==0 && G==0 && B==0 && V==0 && str.front()!=str.back())
			out << "Case #" << t+1 << ": " << str << endl;
		else 
			out << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
	}
}