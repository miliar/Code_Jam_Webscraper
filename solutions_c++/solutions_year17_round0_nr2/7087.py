#include <bits/stdc++.h>
using namespace std;


int main(){

    int t=1,x;
    cin>>t;

    for(int x=1;x<=t;x++){
        string arr;
        cin>>arr;
        int i,j,n,k;
        for(i=arr.size()-1;i>0;i--){
            if(arr[i]<arr[i-1]){
                for(j=i;j<arr.size();j++){
                    arr[j]='9';
                }
                arr[i-1]--;
            }
        }
        bool tmp=0;
        cout<<"Case #"<<x<<": ";
        for(i=0;i<arr.size();i++){
            if(arr[i]=='0' && tmp==0){
                continue;
            }
            else{
                tmp=1;
                cout<<arr[i];
            }
        }
        cout<<endl;
    }

}
