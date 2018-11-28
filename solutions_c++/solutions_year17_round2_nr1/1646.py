 #include <bits/stdc++.h>

#define lp(i,n) for(int i=0; i<n; i++)

#define ll long long
#define pb push_back
#define  mp make_pair
#define pii pair<int,int>
#define ff first
#define ss second
#define nl "\n"

#define EPS 1e-8
#define OO 100000000

#define on(i,n) i=i|(1<<n)
#define off(i,n) i=i& (~(1<<n))

using namespace std;



int n;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    lp(cs,t){
    int d,n;
    cin>>d>>n;
    int posf,poss;
    double slowest_time=-1;
    lp(i,n){
        cin>>posf>>poss;
        double dist_infront=d-posf;
        double time_needed=dist_infront/poss;

        slowest_time=max(slowest_time,time_needed);
    }


    double ans=d/slowest_time;

    cout<<"Case #"<<cs+1<<": ";
    cout<<setprecision(6)<<fixed<<ans<<endl;

    }




}
