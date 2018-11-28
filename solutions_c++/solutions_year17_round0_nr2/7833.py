#include <bits/stdc++.h>
#define ll long long
using namespace std;
int num[20];
int main(){
    int t,k;
    ll ans,n;
    string st;
    cin>>t;
    for(int tc = 1;tc <= t;tc++){
        memset(num,0,sizeof(num));
        cin>>n;
        int ptr = 19;
        ll n1 = n;
        while(n1){
            num[ptr] = n1%10;
            n1/=10;
            ptr--;
        }

        for(int i = 19;i > ptr+1;i--){
            if(num[i] < num[i-1]){
                num[i] = 9;
                num[i-1] -= 1;
            }
        }
        cout<<"Case #"<<tc<<": ";
        int i;
        for(i = ptr+1;i < 20;i++)if(num[i] > 0)break;
        while(i < 20){
            if(num[i] < num[i-1])num[i] = num[i-1];
            cout<<num[i];i++;
        }
        cout<<"\n";
    }
    return 0;
}