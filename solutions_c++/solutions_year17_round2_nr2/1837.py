#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main() {
	ifstream fin;
//	fin.open("B-large.in");
//	fin.open("B-small-attempt0.in");
	fin.open("B-small-attempt1.in");
//	fin.open("B-small-practice.in");
	
	ofstream fout;
//	fout.open("B-large.out");
//	fout.open("B-small-attempt0.out");
	fout.open("B-small-attempt1.out");
//	fout.open("B-small-practice.out");

	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		int N, R, O, Y, G, B, V;
		fin >> N >> R >> O >> Y >> G >> B >> V;
		if(2*(R+O+V) > N || 2*(Y+O+G) > N || 2*(B+V+G) > N || (G > 0 && R < G+1 && R+G != N) || (V > 0 && Y < V+1 && Y+V != N) || (O > 0 && B < O+1 && O+B != N)) {
			fout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		fout << "Case #" << i << ": ";
		int first = 0;
		int last = 0;
		if(G > 0) {
			if(R > G) {
				fout << "R";
				R--;
				if(first == 0)
					first = 1;
			}
			while(G > 0) {
				fout << "GR";
				R--;
				G--;
			}
			last = 1;
		}
		if(V > 0) {
			if(Y > V) {
				fout << "Y";
				Y--;
				if(first == 0)
					first = 2;
			}
			while(V > 0) {
				fout << "VY";
				V--;
				Y--;
			}
			last = 2;
		}
		if(O > 0) {
			if(B > O) {
				fout << "B";
				B--;
				if(first == 0)
					first = 3;
			}
			while(O > 0) {
				fout << "OB";
				B--;
				O--;
			}
			last = 3;
		}
		if(last == 0) {
			if(R <= Y && R <= B)
				last = 1;
			else if(Y <= R && Y <= B)
				last = 2;
			else if(B <= R && B <= Y)
				last = 3;
		}

		while(R > 0 || Y > 0 || B > 0) {
			if(last == 1) {
				if((first != 3 && Y >= B) || Y > B) {
					fout << "Y";
					Y--;
					last = 2;
					if(first == 0)
						first = 2;
				}
				else {
					fout << "B";
					B--;
					last = 3;
					if(first == 0)
						first = 3;
				}
			}
			else if(last == 2) {
				if((first != 3 && R >= B) || R > B) {
					fout << "R";
					R--;
					last = 1;
					if(first == 0)
						first = 1;
				}
				else {
					fout << "B";
					B--;
					last = 3;
					if(first == 0)
						first = 3;
				}
			}
			else if(last == 3) {
				if((first != 2 && R >= Y) || R > Y) {
					fout << "R";
					R--;
					last = 1;
					if(first == 0)
						first = 1;
				}
				else {
					fout << "Y";
					Y--;
					last = 2;
					if(first == 0)
						first = 2;
				}
			}
		}
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

