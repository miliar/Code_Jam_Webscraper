#include <bits/stdc++.h>
#define ll long long int

using namespace std;

struct horse{
    double pos,speed;

    bool operator<(const horse h)const{
        if (pos==h.pos)
            return speed>h.speed;
        return pos>h.pos;
    }

};

horse horses[1005];


int main(){
    freopen("A-large.in","r",stdin); freopen("A-large-1.txt","w",stdout);

    int t;
    cin>>t;

    for(int tc=1;tc<=t;tc++){
        int n,d;
        cin>>d>>n;

        for(int i=0;i<n;i++){
            cin>>horses[i].pos>>horses[i].speed;
        }
        sort(horses,horses+n);

        double slowest=0;
        double tmp1;
        for(int i=0;i<n;i++){
            tmp1=(d-horses[i].pos)/horses[i].speed;
            slowest=max(slowest,tmp1);

        }

        double ans=(d/slowest);

        printf("Case #%d: %.7f\n",tc,ans);


    }

}
