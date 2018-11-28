#include <cstdio>
#include <string>
#include <sstream>
#include <iostream>
#include <cmath>

using namespace std;

int main(){
	string s;
	int ncases;
	long long int n;
	cin >> ncases;
	for(int nc=1; nc<=ncases; nc++){
		cout << "Case #";
		cout << nc;
		cout << ": ";
		stringstream ss;
		cin >> s;
		for(int i=0; i<(int)s.size(); i++){
			if(i && s[i]<s[i-1]){
				int r = i-1;
				//printf(" s[%d]=%c s[%d-1]=%c\n",i,s[i],i,s[i-1]);
				while(r && s[r]==s[r-1]){
					r--;
				}
				//printf(" r %d\n",r);
				s[r] = s[r]-1;
				for(int j=r+1; j<(int)s.size(); j++){
					s[j] = '9';
				}
				break;
			}
		}
		ss << s;
		ss >> n;
		cout << n;
		cout << endl;
	}
}
