#include <bits/stdc++.h>
#define N 100009
#define mod 1000000007
#define inf 1000000000
using namespace std;
typedef long long ll;
typedef double db;

struct zz{
    int t0,t1,who;
    bool operator < (const zz &rhs) const{
        return t0 < rhs.t0;
    }
}a[N];

void solve(int tc){
    printf("Case #%d: ",tc);
    int m,n; scanf("%d%d",&m,&n);
    int p0=0,p1=0;
    for(int i=0;i<m;i++){
        int t0,t1; scanf("%d%d",&t0,&t1);
        a[i]={t0,t1,0};
        p1+=t1-t0;
    }
    for(int i=0;i<n;i++){
        int t0,t1; scanf("%d%d",&t0,&t1);
        a[m+i]={t0,t1,1};
        p0+=t1-t0;
    }n+=m;
    sort(a,a+n);
    //cout << a[i].t0 << "-" << a[i].t1 << endl;
    vector<int> same0,same1,diff;
    int ans=0;
    for(int i=1;i<n;i++){
        if(a[i-1].who == a[i].who){
            if(a[i].who){
                p0+=a[i].t0-a[i-1].t1;
                same0.push_back(a[i].t0-a[i-1].t1);
            }
            else{
                p1+=a[i].t0-a[i-1].t1;
                same1.push_back(a[i].t0-a[i-1].t1);
                //cout << a[i].t0 - a[i-1].t1 << "+\n";
            }
        }
        else{
            diff.push_back(a[i].t0-a[i-1].t1);
            ans++;
        }
        //cout << ans << "--\n";
    }
    if(a[n-1].who == a[0].who){
        if(a[0].who){
            p0+=1440-a[n-1].t1+a[0].t0;
            same0.push_back(1440-a[n-1].t1+a[0].t0);
        }
        else{
            p1+=1440-a[n-1].t1+a[0].t0;
            same1.push_back(1440-a[n-1].t1+a[0].t0);
        }
    }
    else{
        diff.push_back(1440-a[n-1].t1+a[0].t0);
        ans++;
    }
    sort(same0.begin(),same0.end(),greater<int>());
    sort(same1.begin(),same1.end(),greater<int>());
    //for(int x: same0) cout << x << " "; cout << endl;
    //for(int x: same1) cout << x << " "; cout << endl;
    if(p0>720){
        int sum=0;
        for(int i=0;i<same0.size();i++){
            sum+=same0[i]; ans+=2;
            if(sum>=p0-720) break;
        }
    }
    else if(p1>720){
        int sum=0;
        for(int i=0;i<same1.size();i++){
            sum+=same1[i]; ans+=2;
            if(sum>=p1-720) break;
        }
    }
    printf("%d\n",ans);
}

int main(){
    freopen("B-large.in","r",stdin); freopen("out.txt","w",stdout);
    int t; scanf("%d",&t);
    for(int i=1;i<=t;i++) solve(i);
    return 0;
}
