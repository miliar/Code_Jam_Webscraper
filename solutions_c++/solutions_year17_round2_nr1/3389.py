#include <bits/stdc++.h>
#define eps 1E-9
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1;i<=t;i++) {
        int n,d;
        scanf("%d %d",&d,&n);
        vector <long long> k(n);
        vector <long long> s(n);
        for(int i = 0;i<n;i++)
            scanf("%I64d %I64d",&k[i],&s[i]);
        int maxItr = 500;
        int cnt = 0;
        double left = 0,right = 1E9,mid,ans =-1;
        while( cnt < maxItr) {
            mid = (left+right)/2;
            cnt++;
            vector <double> vec;
            vec.clear();
            for(int i = 0;i<n;i++) {
                vec.push_back(mid*s[i] + k[i]);
            }
            for(int i = n-2;i>=0;i--) {
                if(vec[i] > vec[i+1])
                    vec[i] = vec[i+1];
            }
            if(vec[0] < d) {
                left = mid;
            } else {
                ans = mid;
                right = mid;
            }
        }
        printf("Case #%d: %0.8f\n",i,d/ans);
    }
    return 0;
}
