#include<bits/stdc++.h>
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define N 2000
#define inf 1e9
#define km first
#define speed second
#define mod 1000000007
#define ll long long
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.in", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
using namespace std;

//bool cmp(const pair<int,pii>& lhs, const pair<int,pii>& rhs)
//    return lhs.first < rhs.first;
pair<ll,ll> ip[N];
pair<double,double> horse[N];
main(){
    fr;fw;
    int t,n,i,j,cnt=1;
    double d;
    ios::sync_with_stdio(0);
    cin>>t;
    while(t--){
        cin>>d>>n;
        for(i=0;i<n;i++){
            cin>>ip[i].km>>ip[i].speed;
        }
        sort(ip,ip+n);
        for(i=0;i<n;i++){
            horse[i].km=ip[i].km;
            horse[i].speed=ip[i].speed;
        }
        i=n-1;
        j=n-2;
        double time=0;
        double u_speed=horse[i].speed;
        double prev_dist=horse[i].km;
        while(j>=0){
            if(horse[j].speed<=u_speed){
                u_speed=horse[j].speed;
                time=0;
                prev_dist=horse[j].km;
            }
            else{
                horse[j].km += (time*horse[j].speed);
                if(horse[j].km>=prev_dist){
                    j--;
                    continue;
                }
                double x= (prev_dist*horse[j].speed - horse[j].km*u_speed)/(horse[j].speed-u_speed);
                //cout<<x<<"\n";
                if(x<=d){//meet
                    time = (x-horse[j].km)/horse[j].speed;
                    prev_dist=x;

                }
                else{//do not meet
                    u_speed=horse[j].speed;
                    time=0;
                    prev_dist=horse[j].km;
                }
            }
            j--;
        }
        //cout<<u_speed<<" "<<prev_dist<<" "<<time<<"\n";
        double ans=(d*u_speed)/(d-prev_dist+u_speed*time);
        cout<<setprecision(12);
        cout<<"Case #"<<cnt<<": "<<ans<<"\n";
        cnt++;
    }


    return 0;
}


