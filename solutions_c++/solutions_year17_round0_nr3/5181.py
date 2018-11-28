#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;
bool myfunction(int i, int j) { return (i>j); }
long long solve[100][2];
int main() {
	ofstream file;
	file.open("out.in");
	int T;
	cin >> T;
	for (int i = 0;i < T;i++) {
		long long n, k;
		cin >> n >> k;
		vector <long long> vector1;
		vector <long long> vector2;
		vector1.push_back(n);
		long long  z = 0;
		while(k){
			
			if (z % 2 == 0) {

				vector2.clear();
				sort(vector1.begin(), vector1.end(),myfunction);
				for (int j = 0;j < vector1.size() && k;j++) {

					vector2.push_back(vector1[j] / 2);
					vector2.push_back((vector1[j] - 1) / 2);
					k--;
				}

			}
			else {

				vector1.clear();
				sort(vector2.begin(), vector2.end(),myfunction);
				for (int j = 0;j < vector2.size() && k;j++) {
					vector1.push_back(vector2[j] / 2);
					vector1.push_back((vector2[j] - 1) / 2);
					k--;
				}

			}
			z++;
		}
		if((z-1)%2==0){

			solve[i][1] = vector2.back();

			vector2.pop_back();
			solve[i][0] = vector2.back();
			
		}
		else {
			solve[i][1] = vector1.back();
			vector1.pop_back();
			solve[i][0] = vector1.back();
		}
	}
	for (int i = 0;i < T;i++) {
		file << "Case #" << i + 1;
		file << ": ";
		file << solve[i][0] << " " << solve[i][1] << endl;
	}


}