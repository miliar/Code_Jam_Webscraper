#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <iomanip>
#include <math.h>
#define pi	3.14159265358979323846
using namespace std;

int main() {
	ifstream file("A-large.in");
	ofstream out("output.txt");
	int T;
	file >> T;
	for(int t=0; t<T; t++) {
		int a, b;
		file >> a >> b;
		unsigned long long int ans = 0;
		unsigned long long int max = 0;
		unsigned long long int c[a];
		unsigned long long int d[a];
		for(int i=0; i<a; i++) {
			file >> c[i] >> d[i];
		}
		for(int j=0; j<a; j++) {
			vector<unsigned long long int> temp;
			for(int i=0; i<a; i++) {
				if(i == j) {
					max = c[i] * (c[i] + 2*d[i]);
				}
				else {
					temp.push_back(2 * c[i] * d[i]);
				}
			}	
			sort(temp.begin(), temp.end());
			int cnt = b;
			while(cnt > 1) {
				max += temp.back();
				temp.pop_back();
				cnt--;
			}
			if(max > ans) ans = max;
		}
		cout << t+1 << " " << ans << endl;
 		out << "Case #" << t+1 << ": " << fixed << setprecision(9) << pi * ans << endl;	
	}
}