#include <bits/stdc++.h>
using namespace std;

#define FOR(cont,max) for(int (cont)=0;(cont)<(int)(max);(cont)++)

#define I(x) (s[x]-'0')

int main(){
	string s;
	int n;
	cin >> n;
	FOR(caso,n){
		cin >> s;
		for(int it=s.size()-2;it>=0;it--){
			if(I(it)>I(it+1)){
				s[it]--;
				for(int i=it+1;i<s.size();i++)s[i]='9';
			}
		}
		cout << "Case #" << caso+1 << ": " << s.substr(s.find_first_not_of("0")) << endl;
	}
	return 0;
}