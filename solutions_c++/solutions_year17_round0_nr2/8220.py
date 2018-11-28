#include<bits/stdc++.h>
#define ll long long
using namespace std;
int a[100];
int to_arr(ll n){
    ll p,i=0;
    while(n>9){
        p=n%10;
        n/=10;
        a[i]=p;
        i++;
    }
    if(n!=0)
        a[i]=n;
    for(int j=0;j<=i/2;j++){
        swap(a[j],a[i-j]);   
    }
    return i;
}
void change(int len){
    int i;
    for(i=0;i<len;i++){
        if(a[i]>a[i+1]){
            a[i]--;
            for(int k=i+1;k<=len;k++)
                a[k]=9;
            break;
        }
    }
    if(i==len)
        return;
    else 
        change(len);
}
int main(){
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++){
        long long n,k;
        int len;
        k=0;
        cin>>n;
        len=to_arr(n);
        change(len);  
        int s;
        for(int i=0;i<=len;i++){
            if(a[i]){
                s=i;
                break;
            }
        } 
        cout<<"Case #"<<ii<<": ";
        for(int i=s;i<=len;i++)
            cout<<a[i];     
        cout<<endl;
    }
    return 0;
}
