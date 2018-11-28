#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

bool check(string s){
	for(int i = 0; s[i]; i++){
		if(s[i] != '+') return false;
	}
	return true;
}

int main(){
	FILE *f;
	f = fopen("a.txt", "w");
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		string s;
		int b, k = 0;
		cin >> s >> b;
		int size = s.size();
		for(int j = 0; j <= size-b; j++){
			if(s[j] == '-'){
				k++;
				for(int t = j; t < j+b; t++){
					if(s[t] == '-') s[t] = '+';
					else s[t] = '-'; 
				}
			}
		}
		fprintf(f, "Case #%d: ", i);
		if(check(s)) fprintf(f, "%d\n", k);
		else fprintf(f, "IMPOSSIBLE\n");
	}
	fclose(f);
}
