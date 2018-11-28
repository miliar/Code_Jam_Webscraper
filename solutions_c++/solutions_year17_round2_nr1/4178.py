#include <iostream>
#include <vector>
#include <iomanip>
#include <climits>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
#define pb push_back
#define mp make_pair
#define INF LLONG_MAX

int main() {

    freopen("cjinput.txt", "r", stdin);
    freopen("cjoutput.txt", "w", stdout);

    int t;
    cin>>t;
    for(int test=1;test<=t;test++) {

        int d,n;
        cin>>d>>n;
        vector<pair<int,int> > horse(n); 
        for(int i=0;i<n;i++) {
            cin>>horse[i].first>>horse[i].second;
        }

        int curd;
        int curs;
        //int idx=0;
        double ans=0,tmp,tmp1,tmp2,mina;

        if(n==1) {
            ans=(d-horse[0].first);
            ans/=horse[0].second;
        }

        if(n>1) {
        sort(horse.begin(), horse.end());
        tmp1=(d-horse[0].first);
        tmp1/=horse[0].second;
        tmp2=(d-horse[1].first);
        tmp2/=horse[1].second;
        tmp=(horse[1].first-horse[0].first);
        tmp/=(horse[0].second-horse[1].second);
        ans=tmp1;
        if(horse[0].second>horse[1].second) {
            double dist=horse[1].first+horse[1].second*tmp;
            if(dist<d) {
                ans=tmp+(d-dist)/horse[1].second;
            }else {
                ans=tmp1;
            }

        }

        }



        // for(int i=0;i<n;i++) {
        //     cout<<horse[i].first<<" "<<horse[i].second;
        // }

        
        
        ans=d/ans;
        cout<<"Case #"<<test<<": ";
        std::cout << std::fixed;
        std::cout << std::setprecision(6)<<ans<<endl;;
    }
    return 0;
}