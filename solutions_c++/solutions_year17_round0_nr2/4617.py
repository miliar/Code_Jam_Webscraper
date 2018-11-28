// Tidy Numbers

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <iomanip>
#include <sstream>

using namespace std;

int main(){
	int q;
	cin >> q;
	for (int z = 0; z < q; z++){
		long long n;
		cin >> n;
		
		while (true){
			stringstream ss;
			ss << n;
			string s;
			ss >> s;
			//cout << n << endl;
			//getchar();
			bool good = true;
			for (int i = 0; i < s.size()-1; i++){
				if (s[i] > s[i+1]){
					good = false;
					break;
				}
			}
			if (good){
				break;
			}
			
			for (int i = s.size()-1; i > 0; i--){
				if (s[i] < s[i-1] || s[i] == '0'){
					long long sub = 1;
					for (int j = 1; j <= i - s.size()+1; i++){
						sub *= 10;
					}
					//cout << sub << endl;
					long long f = n % sub;
					n -= (f+1);
					break;
				}
			}
		}
		
		//cout << n << endl;
		
		cout << "Case #" << z+1 << ": " << n << endl;
	}
}