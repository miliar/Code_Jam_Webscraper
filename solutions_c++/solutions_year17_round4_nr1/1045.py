#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define CL(A,I) (memset(A,I,sizeof(A)))

#define FOR(i, m, n) for (int i=m; i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)

#define D(X) cout<<"  "<<#X": "<<X<<endl;

using ll=long long;
using ii=pair<ll,ll>;
using vi=vector<ll>;
using vii=vector<ii>;

#define aa first
#define bb second

#define EPS (1e-9)
#define EQ(A,B) (A+EPS>B&&A-EPS<B)

int n,p,cnt[4];


void process(){
    cin>>n>>p;
    CL(cnt,0);
    F(n){
        int x;cin>>x; x%=p;cnt[x]++;
    }

    if(p==2)
        cout<<cnt[0]+(cnt[1]+1)/2<<endl;
    else if(p==3){
        int mm=min(cnt[1],cnt[2]);
        int s=cnt[0]+mm;
        cnt[1]-=mm;
        cnt[2]-=mm;
        cnt[1] = (cnt[1]+2)/3;
        cnt[2] = (cnt[2]+2)/3;
        s+=max(cnt[1],cnt[2]);
        cout<<s<<endl;
    }
    else {
        int m3=min(cnt[1],cnt[3]);
        int s=cnt[0]+cnt[2]/2+m3;
        cnt[2]%=2;
        cnt[1]-=m3;
        cnt[3]-=m3;

        if(cnt[2]==0){
            cnt[1] = (cnt[1]+3)/4;
            cnt[3] = (cnt[3]+3)/4;
            s+=max(cnt[1],cnt[3]);
        }
        else {
            int ccc=0;
            if(cnt[1]>=2)cnt[1]-=2,ccc=1;
            if(cnt[3]>=2)cnt[3]-=2,ccc=1;
            if(ccc==0&&cnt[1]==0&&cnt[3]==0)ccc=1;
            cnt[1] = (cnt[1]+3)/4;
            cnt[3] = (cnt[3]+3)/4;
            s+=max(cnt[1],cnt[3])+ccc;
        }
        cout<<s<<endl;
    }

}

int main() {
    int t;cin>>t;
    F(t){
        cout<<"Case #"<<i+1<<": ";
        process();
    }
    return 0;
}