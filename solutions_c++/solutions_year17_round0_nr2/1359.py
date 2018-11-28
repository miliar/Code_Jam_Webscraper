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

string solve(){
    string s;
    cin>>s;
    int mm=s[0],mmi=0;
    F(s.size()-1){
        if(s[i]>mm)mm=s[i],mmi=i;
        if(s[i]>s[i+1]){
            if(s[i]=='1')s=string(s.size()-1,'9');
            else {
                s[mmi]--;
                FF(s.size()-mmi-1)s[mmi+j+1]='9';
            }
        }
    }
    return s;
}

int main() {
    int t;cin>>t;
    F(t)cout<<"Case #"<<i+1<<": "<<solve()<<endl;
    return 0;
}