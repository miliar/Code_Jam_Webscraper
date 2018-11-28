#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    scanf("%d",&test);
    for(int i = 1;i<=test;i++){
        long long int n;
        scanf("%lld",&n);
        for(long long int k = n;k>=0;k--){
            string num;
            int temp = k;
            while(temp>0){
                int a = temp%10;
                num.push_back(a);
                temp /= 10;
            }
            reverse(num.begin(),num.end());
            int sz = num.size();
            bool chk = true;
            for(int j = 0;j<(sz-1);j++){
                if(num[j]>num[j+1]){
                    chk = false;
                    break;
                }
            }
            if(chk){
                printf("Case #%d: %lld\n",i,k);
                break;
            }
        }
    }
    return 0;
}
