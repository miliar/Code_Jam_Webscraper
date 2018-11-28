#include <iostream>
#include <cstdio>
using namespace std;
typedef long long ll;

ll T,k,n;

struct data{
    ll up;
    ll down;
};

bool big(data a, data b){
    if(a.up*b.down>a.down*b.up){
        return true;
        // a is big
    }
    else{
        return false;
    }
}

int main()
{
    freopen("input2.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int q = 1;q<=T;q++){
        cin>>k>>n;
        data tmp;
        tmp.up = 0;
        tmp.down = 1;
        for(int i = 0;i<n;i++){
            data aa;
            cin>>aa.up>>aa.down;
            aa.up = k-aa.up;
            if(big(aa,tmp)){
                tmp = aa;
            }
        }
        printf("Case #%d: %.6lf\n",q,(double)k*tmp.down/tmp.up);
    }
}
