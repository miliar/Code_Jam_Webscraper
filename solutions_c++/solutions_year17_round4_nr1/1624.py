#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<vector>

using namespace std;

typedef long long int lli;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;


int main(void){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    scanf("%d",&t);
    int v[6];
    for(int c=1;c<=t;++c){
        int n, p;
        scanf("%d %d",&n,&p);
        v[0]=v[1]=v[2]=v[3]=0;
        for(int i=0;i<n;++i){
            int x;
            scanf("%d",&x);
            v[x%p]++;
        }
        int ans = v[0];
        if(p==2){
            ans +=(v[1]+1)/2;
        }else if(p==3){
            int ans2 = min(v[1],v[2]);
            ans+=ans2;
            v[1]-=ans2;
            v[2]-=ans2;
            while(v[1]>0){
                ans++;
                v[1]-=3;
            }
            while(v[2]>0){
                ans++;
                v[2]-=3;
            }
        }else{
            int ans2 = v[2]/2;
            v[2]-=(ans2*2);
            ans+=ans2;
            int ans3 = min(v[1],v[3]);
            v[1]-=ans3;
            v[3]-=ans3;
            ans+=ans3;
            if(v[2]==0){
                while(v[1]>0){
                    ans++;
                    v[1]-=4;
                }
                while(v[3]>0){
                    ans++;
                    v[3]-=4;
                }
            }else{
                ans++;
                if(v[1]>0){
                    v[1]-=2;
                    while(v[1]>0){
                        ans++;
                        v[1]-=4;
                    }
                }else if(v[3]>0){
                    v[3]-=2;
                    while(v[3]>0){
                        ans++;
                        v[3]-=4;
                    }
                }else{
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n",c,ans);

    }
    return 0;
}

