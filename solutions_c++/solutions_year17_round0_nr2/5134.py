#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair

int main(){
	int t,caso = 1;
	scanf("%d",&t);
	while(t--){
		long long x;
		char s[20];
		scanf("%s",s);
		int n = strlen(s);
		while(1){
			int f = 0;
			for(int i = 1; i < n; i++){
				if(s[i] < s[i-1]){
					s[i-1]--;
					f = 1;
					for(int j = i; j < n;j++)
						s[j] = '9';
					break;
				}
			}
			if(f == 0) break;
		}
		x = stoll(s);
		printf("Case #%d: %lld\n",caso,x);
		caso++;
	}
    return 0;
}