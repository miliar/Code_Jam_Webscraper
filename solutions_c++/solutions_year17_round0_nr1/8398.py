#include <iostream>
using namespace std;

int main(void) {
	int t; cin >> t;
	for(int cn=1; cn<=t; cn++) {
		string p; int r=-1, m, ind=-1;
		cin >> p >> m;
		if(p.find('-')==string::npos) r=0;
		for(int i=0; i<p.length(); i++) {
			if(r<0) r=0;
			if(p[i]=='-') 
				if(i+m-1<p.length()) {
					r++;
					for(int j=0; j<m; j++) p[i+j]=(p[i+j]=='+'?'-':'+');
				} else if(i-m+1>0) {
					r++;
					for(int j=0; j<m; j++) p[i-j]=(p[i-j]=='+'?'-':'+');
				}
		}
		if(p.find('-')!=string::npos) r=-1;
		cout << "Case #" << (int) cn << ": ";
		if(r<0) cout << "IMPOSSIBLE" << endl;
		else cout << (int) r << endl;
	}
	return 0;
}
