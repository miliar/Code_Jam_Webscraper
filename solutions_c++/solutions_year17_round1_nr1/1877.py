#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<algorithm>

#define N 30

using namespace std;

char res[N][N];

int main(){
	
	int nc, r, c;
	int caso, i, j;
	string s;
	char enc;

	scanf("%d", &nc);
	for(caso = 1; caso <= nc; caso++){

		for(i = 0; i < r; i++)
			for(j = 0; j < c; j++)
				res[i][j] = '?';


		scanf("%d%d", &r, &c);
		//cout<<r<<" "<<c<<endl;
		for(i = 0; i < r; i++){
			cin>>s;
			enc = '?';
			//cout<<s<<endl;
			for(j = 0; j < c; j++){
				if(s[j] != '?'){
					enc = s[j];
				}
				else{
					if(enc != '?')
						s[j] = enc;
				}
			}
			//cout<<s<<endl;
			for(j = c - 2; j>= 0; j--){
				//cout<<s[j]<<" "<<s[j + 1]<<endl;
				if(s[j] == '?' && s[j + 1] != '?')
					s[j] = s[j + 1];
			}
			
			if(enc == '?'){
				if(i > 0){
					if(res[i-1][0] != '?'){
						for(j = 0; j < c; j++)
							res[i][j] = res[i - 1][j];
					}
				}
			}
			else{
				for(j = 0; j < c; j++)
					res[i][j] = s[j];
			}
			//cout<<s<<endl;
		}

		for(i = r - 2; i >= 0; i--){
			if(res[i][0] == '?' && res[i + 1][0] != '?'){
				for(j = 0; j < c; j++)
					res[i][j] = res[i + 1][j];
			}
		}

		printf("Case #%d:\n", caso);
		for(i = 0; i < r; i++){
			for(j = 0; j < c; j++)
				printf("%c", res[i][j]);
			printf("\n");
		}
	}
	

	return 0;
}
