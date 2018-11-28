#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <vector> 
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>
#include <cassert>

#define INF 1000000000

using namespace std;

typedef long long ll; 
typedef pair<int, int> ii; 
typedef vector<ii> vii; 
typedef vector<int> vi;

int main(){
	int T;
	int k, count, len;
	char words[1040];

	scanf("%d" , &T);
	for(int aux = 0;aux<T;aux++){
		len = 0; count = 0;
		scanf("%s %d", words, &k);
		for(int i =0;words[i]!='\0';i++)
			len++;

		for(int i = 0;i<len; i++){
			if(len - i < k){
				for(int j = i;j<len;j++){
					if(words[j] == '-'){
						count = -1;
						break;
					}
				}
			}
			if(count < 0) break;
			if(words[i] == '+') continue;
			count++;
			for(int j = 0;j< k;j++){
				if(words[i+j] == '+')
					words[i+j] = '-';
				else{
					words[i+j] = '+';
				}
			}
		}
		printf("Case #%d: ", aux+1);
		if(count < 0){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n", count);
		}
	}


	return 0;
}