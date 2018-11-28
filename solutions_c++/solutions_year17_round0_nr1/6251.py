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
const int oo = 100000000;

int solve(string s,int k){
    int n = s.size();
    int ans = 0;
    for(int i=0;i<=(n-k);i++){
        if(s[i]=='+') continue;
        ans++;
        for(int j=0;j<k;j++){
            if(s[i+j]=='+') s[i+j] = '-';
            else s[i+j] = '+';
        }
    }
    for(int i=0;i<n;i++){
        if(s[i]=='-')
            return oo;
    }
    return ans;
}

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int t;
    cin>>t;
    for(int test=1;test<=t;test++){
        string s;
        int k;
        cin>>s>>k;
        int ans = solve(s,k);
        reverse(s.begin(),s.end());
        ans = min(ans,solve(s,k));
        if(ans==oo)
            printf("Case #%d: IMPOSSIBLE\n",test);
        else
            printf("Case #%d: %d\n",test,ans);
    }   

    return 0;
}