/**
Author:  ShivamRathore (Shivam010)
**/
#include <bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        string a="";
        cin>>a;
        int n=a.size();
        if(n==1){
            cout<<"Case #"<<t<<": "<<a<<endl;
            continue;
        }
        bool flag,che;
        for(int c=0;c<n;c++){
            flag=1;che=1;
            for(int i=0;i<n-1;i++){
                if(a[i]>a[i+1]){
                    che=0;
                    if(!flag)
                        a[i+1]='9';
                    else{
                        flag=0;
                        a[i]-=1;
                        a[i+1]='9';
                    }
                }
            }
            if(che)
                break;
        }
        cout<<"Case #"<<t<<": ";
        flag=0;
        for(int i=0;i<n;i++){
            if(flag || a[i]!='0'){
                flag=1;
                cout<<a[i];
            }
        }
        cout<<endl;
    }
    return 0;
}
