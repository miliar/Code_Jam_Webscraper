#include <bits/stdc++.h>
using namespace std;

vector < int > f;
char s[100];
int tc;
int n;
int dp[20][10][2];

int rek ( int p, int last, int dow ){
	//cout << p << " " << last << " " << dow << endl;
	if ( p == n ) return 1;
	int &res = dp[p][last][dow];
	if ( res!= -1 ) return res;
	res = 0;
	if ( dow ){
		res = rek(p+1,9,1);
		return res; 
	} else {
		if ( last <= s[p]-'0' ){
			if ( rek(p+1,s[p]-'0',0) ){
				res = 1;
			}
			if ( res ) return res;
		}
		for ( int i = s[p]-'0'-1; i >= last; i--){
			//cout << p << " " << last << " " << dow << " " << i << endl;
			if ( rek(p+1,i,1) ){
				res = 1;
				return res;
			}
		}
	}
	return res;
}

void dfs( int p, int last, int dow){
	if ( p == n ) return;
	
	if ( dow ){
		printf("9");
		dfs(p+1,9,1);
	} else {
		if( last <= s[p]-'0' && rek(p+1,s[p]-'0',0) ){
			printf("%c",s[p]);
			dfs(p+1,s[p]-'0',0);
			return;
		} 
		
		for ( int i = s[p]-'0'-1; i >= last; i--){
			if ( rek(p+1,i,1) ){
				printf("%d",i);
				dfs(p+1,i,1);
				return;
			}
		}
	}
}

int can( ){
	memset(dp,-1,sizeof(dp));
	int res = rek(0,1,0);
	if ( !res ) return 0;
	dfs(0,1,0);
	printf("\n");
	return 1;
}

int main(){
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++){
		scanf("%s",&s);
		n = strlen(s);
		
		printf("Case #%d: ",t);
		if ( can() ){
			continue;
		} 
		for ( int i = 0; i <n-1; i++){
			printf("9");
		}
		puts("");
	}
	fclose(stdout);
	return 0;
}
