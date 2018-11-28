#include <iostream>
#include <iomanip>
using namespace std;

#define MOD 1000000007

int main()
{
    long long int i,j,t,T;
    string str;
    cin>>T;
    for(t=1;t<=T;t++){
        long long int N,K;
        long long int r[1001];
        long long int h[1001];
        long long int prod[1001];
        long long int max_r,max_h,tmp;
        long double now,then;
        cin>>N;
        cin>>K;
        max_r = 0;
        for(i=0;i<N;i++){
            cin>>r[i];
            cin>>h[i];
            if(max_r<r[i]){
                max_r = r[i];
                max_h = h[i];
            }
            prod[i] = r[i]*h[i];
        }
        for(i=0;i<N-1;i++){
            for(j=i+1;j<N;j++){
                if(prod[j]>prod[i]){
                    tmp = r[i];
                    r[i] = r[j];
                    r[j] = tmp;
                    tmp = h[i];
                    h[i] = h[j];
                    h[j] = tmp;
                    tmp = prod[i];
                    prod[i] = prod[j];
                    prod[j] = tmp;
                }
            }
        }
        long long int flag = 0;
        long double sum = 0;
        long double ans=0;
        long long int r_m = 0,loc = 0;
        for(i=0;i<K;i++){
            sum = sum+prod[i];
            if(r_m<r[i]){
                r_m = r[i];
                loc = i;
            }
            if(r[i] == max_r)flag = 1;
        }
        ans = 2*sum + r[loc]*r[loc];
        if(flag == 0){
            now = r[loc]*r[loc] + 2*r[K-1]*h[K-1];
            then = max_r*max_r + 2*max_r*max_h;
            if(then>now){
                ans = 2*(sum - prod[K-1] + max_r*max_h) + max_r*max_r;
            }
        }
        ans = 3.14159265359 * ans;
        cout<<"Case #"<<t<<": "<<std::setprecision(7) <<fixed<<ans<<endl;
    }
    return 0;
}
