#include <bits/stdc++.h>

using namespace std;

string eval(string s){
	
	

	//cout << s << endl;

	int sz = s.size();

	if(sz==1)
		return s;

	for(int i=sz-1 ; i>=0; i--){
		if(s[i]<s[i-1]){
			s[i] = '9';
			s[i-1]--; 
		}			
	}
	//cout << "salida 1 " << s  << endl;
	for(int i=0; i<sz-1; i++){
		if(s[i] > s[i+1]){
			//s[i]--;
			s[i+1] = '9';
		}
	}
	//cout << "salida 2 " << s  << endl;
	return s;
		
}

void printS(string s){

	bool flag = false;

	int sz = s.size();

	for(int i=0 ; i<sz; i++){
		if(flag){
			printf("%c",s[i] );
		}
		else{
			if(s[i]!='0'){
				flag = true;
				printf("%c",s[i] );
			}
		}
	}

}

int main(){
	int tc;
	scanf("%d",&tc);

	int nx = 1;
	while(tc--){
		string x;
		cin >> x;
		string aux;
		while((aux=eval(x)) != x){
			x = aux;
		}
		printf("Case #%d: ", nx++);
		printS(x);
		printf("\n");
		//cout << x << endl;
	}
}