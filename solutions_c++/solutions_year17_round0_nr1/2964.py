#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

void flip(string *s, int sIndex, int k){
	for(int i=sIndex;i<sIndex+k;i++){
		(*s)[i] = (*s)[i] == '+' ? '-':'+';
	}
}

bool clean(string s){
	for(int i=0;i<s.size();i++) if(s[i] == '-') return false;
	return true;
}

int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		string s;
		int k, flips = 0;
		cin>>s>>k;
		for(int x=0;x<=s.size() - k;x++){
			if(s[x] == '-') {
				flip(&s, x, k);
				flips++;
			}
			//cout<<s<<endl;
		}

		printf("Case #%d: ", i+1);
		if(clean(s)){
			printf("%d\n", flips);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}