//
// Created by sushant on 8/4/17.
//
#include <iostream>

using namespace std;

int main() {
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        long long int n,m;
        int a[20],b[20];
        cin>>n;
        m=n;
        int c=0;
        while(m){
            a[c]=m%10;
            m/=10;
            c++;
        }
        b[0]=a[c-1];
        int i,j,k;
        for(i=1,j=c-2;i<c;i++,j--){
            if(a[j]>=a[j+1]){
                b[i]=a[j];
            }else{
                break;
            }
        }
        i--;
        if(i!=c-1)
        while(b[i]==b[i-1]){
            i--;
        }
        if(i!=c-1) b[i]--;
        for(i=i+1;i<c;i++){
            b[i]=9;
        }
        cout<<"Case #"<<z<<": ";
        int q=0;
        while(!b[q]) q++;
        for(;q<c;q++){
            cout<<b[q];
        }
        cout<<endl;

    }
    return 0;
}
