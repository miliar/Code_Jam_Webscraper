#include <iostream>
#include <fstream>
#include <string>
#define DN 1000
using namespace std;

int T,k;
string n,r;

int ok(string n) {
	int ok=1;
	for(int i=1; i<n.size(); ++i) if(n[i-1]>n[i]) ok=0;
	return ok;
}

int main() {
	ifstream f("b.txt");
	ofstream g("b.out");
	f>>T;
	for(int t=1; t<=T; ++t) {
		r="";
		f>>n;
		for(int i=1; i<n.size(); ++i) r+='9';
		
		if(ok(n)) r=n;
		string c;
		for(int i=0; i<n.size(); ++i) {
			if(n[i]>'1') {
				string aux=c;
				aux+=(n[i]-1);
				for(int j=i+1; j<n.size(); ++j) aux+='9';
				if(ok(aux) && (aux.size()>r.size() || aux>r)) r=aux;
			}
			c+=n[i];
		}

		g<<"Case #"<<t<<": ";
		g<<r;
		g<<'\n';
	}
}