//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define MAXN 1000005
#define ll long long

bool valid(ll num){
    vector<int> v;
    ll it = num;
    while(it){
        v.push_back(it%10);
        it/=10;
    }
    for(int i=v.size()-2;i>=0;i--)
        if(v[i]<v[i+1])
            return false;
    return true;
}

int main(){
    freopen ("B-large.in","r",stdin); 
    freopen ("B-large.out","w",stdout);
    int i,j,t;
    ll n,ans,it,temp;
    scanf("%d",&t);
    for (int tester = 1; tester <= t; ++tester){
        scanf("%lld",&n);
        ans = 0;
        vector<int> v;
        vector<int> v1;
        it = n;
        while(it){
            v.push_back(it%10);
            it/=10;
        }
        for(i=0;i<v.size()-1;i++)
            ans = 10*ans + 9;

        v1 = v;
        temp = 0;
        for(j=v1.size()-1;j>=0;j--)
            temp = 10*temp + v1[j];
        // cout<<temp<<endl;
        if(valid(temp)) 
            ans = max(ans,temp);

        for(i=v.size()-1;i>=0;i--){
            v1 = v;
            if(v1[i]==0) continue;
            v1[i]--;
            for(j=i-1;j>=0;j--)
                v1[j] = 9;
            temp = 0;
            for(j=v1.size()-1;j>=0;j--)
                temp = 10*temp + v1[j];
            // cout<<temp<<endl;
            if(valid(temp)) 
                ans = max(ans,temp);
        }
        printf("Case #%d: %lld\n",tester,ans);
    } 

    return 0;
}