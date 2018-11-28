#include <bits/stdc++.h>
using namespace std;
int t,tc,n,k;

int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    tc=0;
    while(tc++<t){
        int ans=10000;
        vector<int> perm;
        char str[1009];
        scanf("%s ",str);
        scanf("%d",&k);
        n=strlen(str);
        int cnt=0;
        for(int x=0;x<n;x++){
            if(x<n-k+1)
                perm.push_back(x);
            if(str[x]=='+'){
                str[x]='1';
                cnt++;
            }
            else
                str[x]='0';
        }
        //printf("%s\n",str);
        if(cnt==n){
            ans=0;
        }else{
            do{
                bitset<10> bs(str);
                for(int x=0;x<(int)perm.size();x++){
                    //printf("%d",perm[x]);
                    for(int y=perm[x];y<perm[x]+k;y++){
                        bs[y]=1-bs[y];
                    }
                    //printf("%s\n",bs.to_string().c_str());
                    if(bs.count()==n){
                        ans=min(ans,x+1);

                    }
                }
                //printf("\n");
                if(ans!=10000)
                    break;
            }while(next_permutation(perm.begin(),perm.end()));
        }
        //printf("Case #%d: %d\n",tc,ans);
        if(ans!=10000){
            printf("Case #%d: %d\n",tc,ans);
        }else
            printf("Case #%d: IMPOSSIBLE\n",tc);

    }
}
