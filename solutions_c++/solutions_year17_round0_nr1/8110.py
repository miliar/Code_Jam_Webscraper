#include<bits/stdc++.h>
using namespace std;
int T;string S;int K;
int solve();
int main()
{
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		cin >> S >> K;
		int ans=solve();
		if(ans==-1){
			printf("Case #%d: IMPOSSIBLE\n",i);
		}
		else{
			printf("Case #%d: %d\n",i,ans);
		}
	}
	return 0;
}
int solve()
{
	bool f=true;
	for(int i=0;i<(int)S.length();i++){
		if(S[i]=='-'){f=false;}
	}
	if(f){return 0;}
	int res=0;
	for(int i=0;i<=(int)S.length()-K;i++){
		if(S[i]=='-'){
			res++;
			for(int j=0;j<K;j++){
				if(S[i+j]=='-'){
					S[i+j]='+';
				}
				else{
					S[i+j]='-';
				}
			}
		}
	}
	for(int i=0;i<(int)S.length();i++){
		if(S[i]=='-'){
			return -1;
		}
	}
	return res;
}
