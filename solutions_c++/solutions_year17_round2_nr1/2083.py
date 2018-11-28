#include<bits/stdc++.h>
#define N 1005
#define M 1000000007
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define rep(i,s,e) for(int i=s;i<e;i++)
#define drep(i,s,e) for(int i=e-1;i>=s;i--)
#define all(x) (x).begin(),(x).end()
using namespace std;
typedef long long ll;
double dis[N],sp[N],t1,t2,d;
int main(){
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        int n;
        cin>>d>>n;
        for(int i=0;i<n;i++){
            cin>>dis[i]>>sp[i];
            dis[i]=d-dis[i];
        }

        for(int i=n-2;i>=0;i--){
            t1=dis[i+1]/sp[i+1];
            t2=dis[i]/sp[i];
            if(t1>t2){
                sp[i]=dis[i]/t1;
            }
        }
        cout<<setprecision(8)<<fixed;

        cout<<"Case #"<<ii<<": ";
        cout<<(d)*(sp[0]/dis[0])<<endl;
    }
    return 0;
}
