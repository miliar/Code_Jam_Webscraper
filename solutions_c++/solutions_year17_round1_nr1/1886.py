#include <cstdio>
#include <cmath>
#include <climits>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>

int main(){
	int t, r, c, var, flag, linha, varantes;
	std::string s[30];
	scanf("%d", &t);
	for(int cont = 1; cont <= t; cont++){
		scanf("%d%d", &r, &c);
		var = 0;
		linha = 0;
		for(int i = 0; i < r; i++){
			std::cin >> s[i];
			for(int j = 0; j < s[i].size(); j++)
				if(s[i][j] == '?')
					var++;
		}
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(s[i][j] == '?')
					linha = 1;
				else{
					linha = 0;
					break;
				}
			}
			if(linha == 1)
				break;
		}
		//printf("linha %d\n", linha);
		if(r > 1 && linha)
			flag = 1;
		else if(c > 1 && !linha)
			flag = 2;
		while(var > 0){
			if(var == varantes)
				if(flag == 1)
					flag = 2;
				else
					flag = 1;
			varantes = var;
			for(int i = 0; i < r; i++){
				for(int j = 0; j < c; j++){
					if(s[i][j] != '?' && flag == 1){
						if(i + 1 < r && s[i + 1][j] == '?'){
							s[i + 1][j] = s[i][j];
							var--;
						}
						if(i - 1 >= 0 && s[i - 1][j] == '?'){
							s[i - 1][j] = s[i][j];
							var--;
						}
					}
					if(s[i][j] != '?' && flag == 2){
						if(j + 1 < c && s[i][j + 1] == '?'){
							s[i][j + 1] = s[i][j];
							var--;
						}
						if(j - 1 >= 0 && s[i][j - 1] == '?'){
							s[i][j - 1] = s[i][j];
							var--;
						}
					}
				}
			}
		}
		printf("Case #%d:\n", cont);
		for(int i = 0; i < r; i++){
			std::cout << s[i] << std::endl;
			s[i].clear();
		}
	}
    return 0;
}
