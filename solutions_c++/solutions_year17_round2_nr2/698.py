#include <iostream>
#include <string>
using namespace std;

int n;
int r,o,y,g,b,v;
char s[2000];

int riempi(int pos, char c, int num){
	while(num>0){
		s[pos] = c; num--;
		pos = pos+2; 
		if(pos>=n) pos = 1; 
	}
	return pos;
}

void test_case(){
	cin >> n;
	cin >> r >> o >> y >> g >> b >> v;
	for(int i=0; i<2000; i++) s[i] = 0;
	
	int pos = riempi(0,'R',r);
	if(y<b){
		pos = riempi(pos, 'Y', y);
		pos = riempi(pos, 'B', b);
	}else{
		pos = riempi(pos, 'B', b);
		pos = riempi(pos, 'Y', y);
	}
	bool ok = true;
	for(int i=0; i<n-1; i++) if(s[i]==s[i+1]) ok=false;
	if(s[n-1]==s[0]) ok = false;
	
	if(ok) cout << s << endl;
	else cout << "IMPOSSIBLE" << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		test_case();
	}
	return 0;
}
