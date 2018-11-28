#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>

#define ll unsigned long long int

using namespace std;


int main(){
	int t,caso,k;
	string cad;
	scanf("%d",&t);
	caso = 1;
	while(t--){
		cin >> cad >> k;
		int flips = 0;
		int pos = 0;
		while(pos <= cad.size() - k){
			if(cad[pos] == '+'){
				pos++;
				continue;
			}
			else{
				for(int r = pos;r < pos + k;r++)
					cad[r] = (cad[r] == '+')? '-':'+';
				 flips++;
			}
		}
		bool flag = true;
		for(int i = 0;i < cad.size() && flag;i++){
			if(cad[i] == '-') flag = false;
		}
		if(flag){
			printf("Case #%d: %d\n",caso++,flips);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",caso++);
		}		
	}
	return 0;
}
