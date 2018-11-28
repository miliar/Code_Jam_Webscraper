#include <bits/stdc++.h>
using namespace std;
int main() {
    ifstream inp;
    inp.open("input");
    int t;
    inp>>t;
    for(int i=1;i<=t;i++){
        cout<<"Case #"<<i<<":"<<endl;
        int r,c;
        inp>>r>>c;
        string arr[r];
        for(int j=0;j<r;j++){
            inp>>arr[j];
        }
        for(int j=0;j<r;j++){
            for(int k=1;k<c;k++){
                arr[j][k]=(arr[j][k]=='?')?arr[j][k-1]:arr[j][k];
            }
            for(int k=c-2;k>-1;k--){
                arr[j][k]=(arr[j][k]=='?')?arr[j][k+1]:arr[j][k];
            }
        }
        for(int ji=0;ji<r;ji++){
            if(arr[ji][0]=='?'){
                if(ji==0){
                    arr[ji]=arr[ji+1];
                } else{
                    arr[ji]=arr[ji-1];
                }
            }
        }
        for(int x=0;x<r;x++){
            cout<<arr[x]<<endl;
        }
    }
    return 0;
}