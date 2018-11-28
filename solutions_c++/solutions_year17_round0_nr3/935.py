#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi, ll>
#define f first
#define s second
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define fre freopen("in.txt","r",stdin)
int cnt = 1;
void print(string s) {
    cout << "Case #"<<cnt<<": "<<s<<"\n";
    cnt++;
}
void print(ll x) {
    cout << "Case #"<<cnt<<": "<<x<<"\n";
    cnt++;
}
void print(ll x,ll y) {
    cout << "Case #"<<cnt<<": "<<x<<" " <<y<<"\n";
    cnt++;
}
int main() {
    freopen("C-large.in","r",stdin);
   freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    while(t--) {
        ll N,K;
        cin >> N >> K;

        map<ll,ll>M;
        M[N]=1;

        while(1) {
            ll p1 = M.rbegin()->f;
            ll p2 = M.rbegin()->s;
            M.erase(M.find(p1));
            if(p2>=K) {
                p1--;
                print((p1+1)/2,p1/2);
                break;
            }
            K-=p2;
            p1--;
            M[p1/2]+=p2;
            M[(p1+1)/2]+=p2;
        }
    }
}
