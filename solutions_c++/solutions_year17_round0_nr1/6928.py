#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <utility>
#include <map>
#include <vector>
#include <climits>
#include <set>
#include <algorithm>
 
using namespace std;

int const MAX = 1000;
char S[MAX + 1];

int main(){
	int t;
	scanf("%d", &t);
	for(int p = 1; p <= t; p++){	
		scanf("%s", S);
		int K;
		scanf("%d", &K);
		int n = strlen(S);
		bool fg = 1;
		int cnt = 0;
		for(int i = 0; i < n; i++){
			if(S[i] == '-'){
				if(i + K - 1 >= n){
					fg = 0;
					break;
				}
				cnt += 1;
				for(int j = i; j <= i + K - 1; j++)
					S[j] = ( S[j] == '+' ? '-' : '+');
			}		
		}
		printf("Case #%d: ", p);
		if(fg == 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", cnt);
	}		
	return 0;
}