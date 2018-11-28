#include<bits/stdc++.h>
using namespace std;
char s[30];
int main(){
	freopen("B-large.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	for(int tt = 1; tt <= t; tt ++){
		scanf("%s" , s);
		int n = strlen(s) , flag = 0;
		string res = "" , S = s;
		for(int i = 0 ;i < n ;i ++){
			char x = s[i];
			if(n == 1){
				res += (x);
			}
			else {
				int idx = -1;
				for(int ii = 1 ; ii < 10 ; ii ++){
					if(res.size() && char(ii + '0') < res[i - 1] )
						continue;
					string check = res;
					for(int iii = 0 ; iii < n - res.size() ; iii ++)
						check += char(ii + '0');
					if(check <= S)
						idx = ii;
				}
				if(idx == -1){
					flag = 1;
					break;
				}
				else 
					res += char(idx + '0');
			}
		}
		if(flag == 1){
			res = "";
			for(int i = 0 ;i < n - 1; i ++)
				res += '9';
		}
		printf("Case #%d: %s\n" , tt , res.c_str() );
	
	}

}
