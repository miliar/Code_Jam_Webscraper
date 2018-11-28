#include <iostream>

using namespace std;

char foo[1001];
int k;

int main() {	int t;
    freopen("./A-large.in.txt", "r", stdin);
	freopen("./A-large.out.txt", "w", stdout);
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		scanf("%s", foo);
		scanf("%d", &k);
		int n = strlen(foo);
		int ans = 0;
		bool noWay = false;		
		while(n > 0){

			if(foo[n - 1] == '+'){
				n--;
				continue;
			} 
			
			if(n > 0 && k > n){
				noWay = true;
				break;
			}
			
			for(int i = 0; i < k; ++i){
				if(i == 0){
					ans++;
				}
				if(foo[n - 1 - i] == '-'){
					foo[n - 1 - i] = '+';
				}
				else{
					foo[n - 1 - i] = '-';
				}
			}			
		}
		
		if(noWay){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n", ans);
		}
	}
	
	return 0;
}