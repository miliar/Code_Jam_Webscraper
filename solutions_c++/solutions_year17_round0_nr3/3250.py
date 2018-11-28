#include <bits/stdc++.h>
using namespace std;
long long int l(long long int k){
    return k/2;
}
long long int s(long long int k){
    return (k-1)/2;
}
int main(){
    ofstream out;
    out.open("output");
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        out<<"Case #"<<z<<": ";
        long long int n,k;
        cin>>n>>k;
        long long int arr[]={n+1,n,0,1};
        while(1){
            k-=(arr[2]+arr[3]);
            if(k<=0){
                break;
            }
            if(arr[0]%2){
                arr[2]+=(arr[2]+arr[3]);
            }else{
                arr[3]+=(arr[2]+arr[3]);
            }
            arr[0]/=2;
            arr[1]=arr[0]-1;
        }
        if(k>(-1)*arr[3]){
            out<<l(arr[1])<<" "<<s(arr[1])<<endl;
        }else{
            out<<l(arr[0])<<" "<<s(arr[0])<<endl;
        }
    }
    out.close();
    return 0;
}