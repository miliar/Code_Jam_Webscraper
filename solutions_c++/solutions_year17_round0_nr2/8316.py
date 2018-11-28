#include <bits/stdc++.h>

using namespace std;

int k;
string str;

void f(int index){

	if(index == str.size()) return;

	if(str[index] >= str[index-1])
		f(index+1);

	else{
		index--;
		while(1){
			if(index == 0){
				break;
			}
			if(str[index] == '0')
				index--;
			else if(str[index] == str[index-1])
				index--;
			else break;
		}
		
		str[index]--;
		
		for(int i = index+1; i < str.size(); i++){
			str[i] = '9';
		}

		f(index+1);
	}

}

int main(){

	int n;

	scanf("%d", &n);

	for(int casos = 1; casos <= n; ++casos){

		char aux[50];

		scanf(" %s", aux);

		str = aux;

		f(1);

		printf("Case #%d: ",casos);

		bool jafoi = false;

		for(auto x: str){
			
			if(x == '0' and jafoi) printf("0");

			else if(x != '0'){
				jafoi = true;
				printf("%c",x );
			}
		}

		printf("\n");

	}

	return 0;
}