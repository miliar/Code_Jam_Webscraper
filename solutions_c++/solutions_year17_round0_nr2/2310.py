#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<map>
#include<cmath>
#define ll long long
using namespace std;
int T,a,l;
ll n;
char s[30],r[30];
int main(){
	scanf("%d",&T);
	for (int I=1;I<=T;I++){
		scanf("%s",s);
		l=strlen(s);
		for (int k=1;k<=l;k++){
			for (int i=1;i<l;i++)
				if (s[i]<s[i-1]){
					s[i-1]--;
					for (int j=i;j<l;j++) s[j]='9';
				}
		}
		sscanf(s,"%lld",&n);
		printf("Case #%d: %lld\n",I,n);
	}
    return 0;
}

