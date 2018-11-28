/*************************************************************************
    > File Name: qua1.cpp
    > Author: Yuchen Wang
    > Mail: wyc8094@gmail.com 
    > Created Time: Sat Apr  8 10:57:50 2017
 ************************************************************************/

#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const int maxn = 1005;

int n,k,t;
char s[maxn];
int runtime[maxn*2];
int ans,run;

int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("att.out","w",stdout);
	int i,j=0;

	cin >> t;
	while(t--){
		cout << "Case #" << ++j << ": ";
		scanf("%s %d",s,&k);
		n = strlen(s);
		memset(runtime,0,sizeof(runtime));
		ans = run = 0;

		for(i=0;i<n;i++){
			run += runtime[i];
			if(s[i] == '-' && (run&1)==0){
				runtime[i+k]--;
				ans++;
				run++;
			}
			else if(s[i] == '+' && (run&1)){
				runtime[i+k]--;
				ans++;
				run++;
			}
		}
		run += runtime[n];

		if(run)cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}

