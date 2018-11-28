#include <bits/stdc++.h>
using namespace std;

int n;


int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int cs = 1;
    while(t--){
        printf("Case #%d: ",cs++);
        scanf("%d",&n);
        int ans =0  ;
        for(int i=1;i<=n;i++){
            vector<int> dig;
            int num = i;
            while(num > 0){
                dig.push_back(num%10);
                num/=10;
            }
            int si = dig.size();
            bool can = 1 ;
            for(int i=si-1;i>0;i--){
                if(dig[i] > dig[i-1])
                    can = 0;
            }
            if(can)
                ans = i;
        }
        printf("%d\n",ans);
    }
    return 0;
}
