#include <bits/stdc++.h>
#define F first
#define S second
#define pb push_back
#define mk make_pair
#define ll long long
using namespace std;
typedef pair<int, int> pii;
const int N=1004;

char s[N];
int main(){
	int test,t,n,i,j,k,ans,first;
	scanf("%d",&test);
	for(t=0;t<test;++t){
		scanf(" %s %d",s,&k);
		n=strlen(s);	ans=0;
		for(i=0;i<n;){
			if(s[i]=='+')
				++i;
			else{
				++ans;
				if(i+k-1>=n){
					ans=-1;
					break;
				}
				first=i+k;
				for(j=i;j<i+k;++j){
					if(s[j]=='+'){
						s[j]='-';
						if(first==i+k)
							first=j;
					}
					else
						s[j]='+';
				}
				i=first;
			}
		}
		printf("Case #%d: ",t+1);
		if(ans!=-1)
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");
	}	
	return 0;
}