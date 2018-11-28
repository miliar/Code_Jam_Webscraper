#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
string flip(string s, int pos, int k){
	int i;
	for(i=pos;i<pos+k;i++){
		if(s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
	return s;
}

int check(string s){
	int i;
	for(i=0;i<s.size();i++)
		if(s[i] == '-') return 0;
	return 1;
}
int main(){
	int i, j, t, k;
	string s;
	FILE *fp;
		fp = fopen("large.out", "w");
	cin.sync_with_stdio(false);
	cin >> t;
	for(i=1;i<=t;i++){
		int flipped = 0, done = 0;
		cin >> s >> k;
		for(j=0;j<=s.size() - k;j++){
			if(check(s)){
				done = 1;
				break;
			}
			if(s[j] == '-'){
				s = flip(s, j, k);
				flipped++;
			}
		}
		
		fprintf(fp, "Case #%d: ", i);
		done = check(s);
		if(done){
			fprintf(fp, "%d\n", flipped);
		}
		else{
			fprintf(fp, "IMPOSSIBLE\n");
		}
	}
	fclose(fp);
}