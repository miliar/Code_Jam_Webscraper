#include<bits/stdc++.h>
using namespace std;

int n,m;
char str[100001];
int pm[100001];

int main(){
	int turn;
	scanf("%d",&turn);
	for(int t = 1; t <= turn;t++){
		scanf("%s",str);
		scanf("%d",&m);
		n = (int)strlen(str);
		for(int i=0;i<n;i++){
			pm[i] = (str[i] == '+') ? 1 : 0;
		}
		int cnt = 0;
		for(int i=0;i<=n-m;i++){
			if(!pm[i]){
				for(int j=i;j<i+m;j++) pm[j] = !pm[j];
				cnt++;
			}
		}
		int ans = 1;
		for(int i=0;i<n;i++){
			ans = ans & pm[i];
		}
		printf("Case #%d: ", t);
		if(ans) printf("%d\n",cnt);
		else printf("IMPOSSIBLE\n");
	}
}
