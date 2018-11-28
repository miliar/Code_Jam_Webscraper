//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
char s[1003];
int main(void){
    int t;
    scanf("%d",&t);
    for(int hh=1;hh<=t;hh++){
		scanf("%s",s);
		int k;
		scanf("%d",&k);
		int n=strlen(s);
		int i=0;
		int cnt=0;
		for(i=0;i+k<=n;i++){
			if(s[i]=='-'){
				for(int j=i;j<i+k;j++){
					if(s[j]=='+') s[j]='-';
					else s[j]='+';
				}
				cnt++;
				//printf("%d %s\n",i,s);
			}
		}
		bool ok=true;
		for(i=0;i<n;i++)
			if(s[i]=='-') ok=false;
		if(ok) printf("Case #%d: %d\n",hh,cnt);
		else printf("Case #%d: IMPOSSIBLE\n",hh);
	}
    return 0;
}
