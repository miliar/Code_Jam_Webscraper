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
		n = (int)strlen(str);
		int is_same = 0;
		int errwhere = 0;
		for(int i=1;i<n;i++){
			if(str[i-1] < str[i]){
				is_same = i;
			}else if(str[i-1] > str[i]){
				errwhere = i;
				break;
			}
		}
		if(errwhere){
			str[is_same]--;
			for(int i = is_same+1;i<n;i++){
				str[i] = '9';
			}
		}
		int where_start = 0;
		for(;where_start<n && str[where_start] == '0';where_start++);
		printf("Case #%d: %s\n", t, str+where_start);
	}
}
