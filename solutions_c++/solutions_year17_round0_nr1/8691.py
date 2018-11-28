#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
        string s;
        cin>>s;
        int k;
        cin>>k;
        int n=s.size();
        int ans=0;
        int i,j;
        for(i=0; i+k<=n; i++){
            if(s[i]=='-'){
                ans++;
                for(int l=0; l<k; l++)
                s[i+l]=(s[i+l]=='-'?'+':'-');
            }
        }
        bool flag=1;
        for(j=i; j<n; j++){
            if(s[j]=='-')
                flag=0;
        }
        if(flag)
        printf("Case #%d: %d\n",t,ans);
        else
        printf("Case #%d: IMPOSSIBLE\n",t);
	}
	return 0;
}
