#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long
#define F first
#define S second
#define pp pair<int,int>
using namespace std;


int main(){
    freopen("A-large.in","r",stdin); freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int D,N;
        cin>>D>>N;
        double tmax=0;
        for(int i=0;i<N;i++){
            int k,s;
            cin>>k>>s;
            double t=(D-k)/(double)s;
            if(t>tmax)tmax=t;
        }

        double ans=D/tmax;


        cout<<"Case #"<<t<<": ";
        printf("%.9lf\n",ans);
    }
    return 0;
}
