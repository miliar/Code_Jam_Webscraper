#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("C:\\Users\\lenovo\\Downloads\\C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, cas=0;
    long long n, k, magic_number, x, y, max_val, min_val;
    cin>>T;
    while(T--){
        cin>>n>>k;
        magic_number=1;
        for(int i=0; i<63; ++i){
            if(magic_number>k)
                break;
            magic_number<<=1;
        }
        n-=(magic_number-1);
        if(n<=0){
            cout<<"Case #"<<++cas<<": 0 0"<<endl;
        }else{
            x=n/magic_number;
            y=n%magic_number;
            max_val=min_val=x;
            k-=(magic_number/2-1);
            if(k<=y)
                ++max_val;
            if(magic_number/2+k<=y)
                ++min_val;
            cout<<"Case #"<<++cas<<": "<<max_val<<" "<<min_val<<endl;
        }
    }
    return 0;
}
