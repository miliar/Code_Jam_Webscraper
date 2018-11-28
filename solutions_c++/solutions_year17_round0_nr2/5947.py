#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second

using namespace std;

int main(int argc, char* argv[]){
	int T;
	char num[100];
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		scanf("%s", num);
		int len = strlen(num);
		int mod = -1;
		for(int i = 1; i < len; i++)
			if(num[i] < num[i-1]){
				for(int j = i-1; j >= 0; j--){
					mod = j+1;
					if(num[j] != '0'){
						num[j] -= 1;
						if(j-1>=0 && num[j]>=num[j-1])
							break;
					}	
				}
				for(int j = mod; j < len; j++)
					num[j] = '9';
				break;
			}
		int s;
		for(s = 0; s < len; s++)
			if(num[s] != '0') break;
		printf("%s\n", num+s);	
	} 
    return 0;
}
