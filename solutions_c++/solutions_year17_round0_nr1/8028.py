#include<iostream>
#include<cstdio>
#include<string>
#include<cmath>
#include<algorithm>

using namespace std;

int main(){

	int nc;
	string s;
	int k;
	int caso, i, j, r, l, cont;
	bool imposible;

	scanf("%d\n", &nc);

	for(caso = 1; caso <= nc; caso++){
		cin>>s>>k;
		
		l = s.length();
		i = 0;		
		cont = 0;
		imposible = false;

		while(i < l){

			j = i;		
			while(j < l){
				if(s[j] == '-')
					break;
				j++;
			}

			if(j >= l) break;
			if(s[j] == '+') break;

			if( j + k - 1 < l){
				
				cont++;

				for(r = j; r < j + k; r++){
					if(s[r] == '-')
						s[r] = '+';
					else
						s[r] = '-';
				}
			}
			else{
				imposible = true;
				break;
			}

			i = j + 1;
		}

		printf("Case #%d: ", caso);

		if(imposible) printf("IMPOSSIBLE\n");
		else printf("%d\n", cont);

	}


	return 0;
}
