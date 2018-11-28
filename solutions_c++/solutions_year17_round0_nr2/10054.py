#include<iostream>
#include<string>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main() {
	int t,s;
	string a;
	ifstream in ("1.in");
	ofstream out ("1.out");
	bool ok;
	if(in.is_open()) {
		getline(in,a);
		t=stoi(a);
		for(int i=1; i<=t; i++) {
			getline(in,a);
			ok=false;
			while(!ok) {
				ok=true;
				for(int i=1; i<a.size(); i++) {
					if(a[i-1]>a[i]) {
						ok=false;
						break;
					}
				}
				if(!ok) {
					s=stoi(a);
					s--;
					a=to_string(s);
				}
			}
			out<<"Case #"<<i<<": "<<a<<endl;
		}
		in.close();
	}
	else cout << "Unable to open file";
}
