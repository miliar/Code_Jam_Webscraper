#include <bits/stdc++.h>

using namespace std;

#define foru(i,a,b) for(int i=a; i<=b; i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define reset(a,b) memset(a,b,sizeof(a))
#define ha return 0
typedef long long int64;

int64 n,k;
struct p
{
  int64 mi,ma;
};

p cal(int64 n,int64 k){
    p ans;
    if (k==1) {
        ans.mi = (n-1)/2;
        ans.ma = n-1-ans.mi;
        return ans;
    }

    k--;
    if (n%2==1){
        if (k%2==0) return cal(n/2, k/2);
        return cal(n/2, k-k/2);
    }

    if (n%2==0){
        if (k%2==0) return cal((n-1)/2, k/2);
        return cal(n-1-(n-1)/2, k-k/2);
    }
}

int main()
{
    freopen("input.inp","r",stdin);
    freopen("output.out","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int test;
    cin>>test;
    int cnt=0;
    while (test--){
        cin>>n>>k;
        p res = cal(n,k);
        cnt++;
        cout<<"Case #"<<cnt<<": "<<res.ma<<" "<<res.mi<<"\n";
    }

    return 0;
}
