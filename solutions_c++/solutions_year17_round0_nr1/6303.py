#include<bits/stdc++.h>
using namespace std;
char S[20000];
int main(){
	freopen("A-large.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	for(int i = 1; i <= t; i ++){
		int no;
		scanf("%s%d" , S , &no);
		int n = strlen(S);
		vector< int > A(n);
		int cnt = 0 , flag = 0;
		for(int i = 0 ;i < n ;i ++){
			if((S[i] == '+' && A[i] % 2 == 1) || (S[i] == '-' && A[i] % 2 == 0) ){
				if(n - i >= no){
					cnt ++;
					for(int l = i ; l < i + no ; l ++)
						A[l] ++;
				}
				else flag = 1;
			}
		}
		printf("Case #%d: " , i);
		if(flag)puts("IMPOSSIBLE");
		else printf("%d\n" , cnt);
	}

}
