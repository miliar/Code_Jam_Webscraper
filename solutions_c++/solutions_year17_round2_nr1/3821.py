#include<bits/stdc++.h>

using namespace std;

vector<double> lol;

int main(){
    //freopen("A-large.in","r",stdin);
   // freopen("contl.txt","w",stdout);
    int t;
    cin>>t;
    for(int O=0;O<t;O++){
            lol.clear();
            double d,n;
            cin>>d>>n;
            for(int i=0;i<n;i++){
                double x,y;
                cin>>x>>y;
                int z = d-x;
                lol.push_back((double)z/y);
            }
            sort(lol.begin(),lol.end());
            reverse(lol.begin(),lol.end());
            double ans = d/lol[0];
            cout<<fixed<<setprecision(6)<<"Case #"<<O+1<<": "<<ans<<endl;

    }

}
