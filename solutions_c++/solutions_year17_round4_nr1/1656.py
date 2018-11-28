#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <string>

using namespace std;
vector<int> G;
int main()
{
    freopen("data.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){
        int n,p,x;
        G.clear();
        scanf("%d%d",&n,&p);
        for(int i=1;i<=n;i++) {
            scanf("%d",&x);
            G.push_back(x);
        }
        int res=0;
        if(p==2){
            int odd=0;
            for(int i=0;i<n;i++){
                if(G[i]%2==0){
                    res++;
                }
                else {
                    odd++;
                }
            }
            res+=(odd+1)/2;
        }
        else if(p==3){
            int one=0,two=0;
            for(int i=0;i<n;i++){
                if(G[i]%3==0){
                    res++;
                }
                else if(G[i]%3==1){
                    one++;
                }
                else if(G[i]%3==2){
                    two++;
                }
            }
            if(one<two) swap(one,two);
            res+=two;
            one-=two;
            res+=(one/3);
            if(one%3) ++res;
        }
        printf("Case #%d: %d\n",kase,res);

    }
    return 0;
}
