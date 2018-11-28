#include<bits/stdc++.h>
using namespace std;

#define lli long long
#define pb push_back
#define mp make_pair
#define gc getchar_unlocked
#define lld "%I64d"
#define DEBUG(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define mod 1000000007

const int lmt=1000005;

bool good(lli n){
    vector<int> dig;
    while(n>0){
        dig.pb(n%10LL);
        n /= 10LL;
    }
    reverse(dig.begin(),dig.end());
    int last = dig[0];
    for(int i=1;i<dig.size();i++){
        if(dig[i]<last) return false;
        last=dig[i];
    }
    return true;
}

lli solve(lli n){
    vector<int> ndig;
    while(n>0){
        ndig.pb(n%10);
        n /= 10LL;
    }
    reverse(ndig.begin(),ndig.end());

    lli ans = 0;
    for(int i=0;i<ndig.size();i++){
        vector<int> newDig;
        if(ndig[i]==0) continue;
        for(int j=0;j<i;j++)
            newDig.pb(ndig[j]);
        newDig.pb(ndig[i]-1);
        for(int j=i+1;j<ndig.size();j++)
            newDig.pb(9);
        bool good = true;
        for(int j=1;j<newDig.size();j++){
            if(newDig[j]<newDig[j-1]){
                good = false;
                break;
            }
        }
        if(good){
            lli temp=0;
            for(int j=0;j<newDig.size();j++)
                temp = temp*10 + newDig[j];
            ans = max(ans,temp);
         }
    }
    return ans;
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
        lli n;
        scanf("%lld",&n);
        if(good(n)){
            printf("Case #%d: %lld\n",test,n);
            continue;
        }
        if(good(n-1)){
            printf("Case #%d: %lld\n",test,n-1);
            continue;
        }
        printf("Case #%d: %lld\n",test,solve(n));        
    }   
    return 0;
}