#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
//#pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
using namespace __gnu_pbds;
typedef pair<int,int> par;
typedef pair<par,int> pr;

bool mp[1005][1005];
int go[1005];
bool used[1005];
vector<int>nod[2];
int cnt[2][1005];
int main(){
    int t,T=0;
    scanf("%d",&t);
    while(t--){T++;
        int n,c,m;
        scanf("%d%d%d",&n,&c,&m);
        for(int i=0;i<c;i++)
            nod[i].clear();
        int ans=0,ans2=0;
        memset(cnt,0,sizeof(cnt));
        for(int i=0;i<m;i++){
            int a,b;
            scanf("%d%d",&a,&b);b--;
            //cnt[b][a]++;
            nod[b].push_back(a);
            }
        memset(mp,0,sizeof(mp));
        int sz0=nod[0].size(),sz1=nod[1].size();
        for(int i=0;i<sz0;i++){
            for(int j=0;j<sz1;j++)
                if(nod[0][i]!=nod[1][j])
                    mp[i][j]=1;
            }
        memset(go,-1,sizeof(go));
        int N=max(sz0,sz1);
        for(int i=0;i<N;i++){
            memset(used,0,sizeof(used));
            function<bool(int)>F=[&](int now)->bool{
                for(int j=0;j<N;j++)
                    if(mp[now][j] && !used[j]++ && (!~go[j]||F(go[j])) ){
                        go[j]=now;
                        return 1;
                        }
                return 0;
                };
            ans+=F(i);
            }
        for(int i=0;i<sz1;i++)
            if(go[i]==-1){
                cnt[1][nod[1][i]]++;
                }
            else{
                nod[0][go[i]]=0;
                }
        for(int i=0;i<sz0;i++)
            cnt[0][nod[0][i]]++;

        //printf("~%d %d\n",ans,ans2);
        for(int i=2;i<=n;i++)
            if(cnt[0][i]&&cnt[1][i]){
                int k=min(cnt[0][i],cnt[1][i]);
                ans+=k;
                ans2+=k;
                cnt[0][i]-=k;
                cnt[1][i]-=k;
                }
        for(int i=1;i<=n;i++){
            ans+=cnt[0][i]+cnt[1][i];
            }
        printf("Case #%d: %d %d\n",T,ans,ans2);
        }
    return 0;
    }
//5 6 7 8 9
//1 2 3 4 5
//1 1 1 1 1 1 2 3
//2 2 2 2 3 3 3 3

//1 1
