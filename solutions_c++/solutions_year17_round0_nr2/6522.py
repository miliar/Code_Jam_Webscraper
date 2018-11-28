#include <iostream>
#include <cstdio>
using namespace std;
int dig[24];
int main(){
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int j=0; j<t; ++j){
        unsigned long long a, b;
        cin>>a;
        b=a;
        int i;
        for (i=0; b>0; ++i){
            dig[i]=b%10;
            b/=10;
        }
        int k;
        for (k=i-1; k>0; --k){
            if (dig[k]>dig[k-1]){
                break;
            }
        }
        cout<<"Case #"<<j+1<<": ";
        if (k==0){cout<<a<<endl;continue;}
        for (k; k<i; ++k){
            if (k==i-1 || dig[k]>dig[k+1]){
                break;
            }
        }
        unsigned long long ans=0;
        for (int l=i-1; l>k; --l){
            ans*=10; ans+=dig[l];
        }
        ans*=10; ans+=dig[k]-1;
        for (int l=k-1; l>=0; --l){
            ans*=10; ans+=9;
        }
        cout<<ans<<"\n";
    }
    return 0;
}
