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
		scanf("%s", words);
		len = strlen(words);
		for(int i = len-1;i>=0; i--){
			if(words[i-1] > words[i]){
				words[i-1]--;
				for(int j = i;j<len;j++)
					words[j] = '9';
			}
		}
		if(words[0] == '0'){
			for(int i = 0;i<len;i++)
				words[i] = words[i+1];
		}
		printf("Case #%d: ", aux+1);
		printf("%s\n", words);
	}


	return 0;
}