#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int ctoi(const char c){ 
	if ( c < '0' || c > '9') {
		return 0;
	} else {
		return (int)(c-'0');
	} 
};
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);
	cout << fixed;

	int T;
	cin >> T;
	for(int to=1;to<=(int)T;++to){
		cout << "Case #"<< to <<": ";
		string s;
		cin >> s;
		for(int i=0; i<s.size()-1; i++){
			int l,m;
			l = ctoi(s[i]);
			m = ctoi(s[i+1]);
			if(l > m) {
				s.replace(i,1,to_string(l-1));
				for(int j=i+1;j<s.size();j++){
					s.replace(j,1,"9");
				}
				i-=2;
			}
		}
		int idx=0;
		for(int k =0 ;k<s.size();k++){
			if(ctoi(s[k])!=0){
				idx=k;
				break;
			}
		}
		cout << s.substr(idx)<< "\n";
	}
#ifdef LOCAL_DEFINE
	cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
	return 0;
}

