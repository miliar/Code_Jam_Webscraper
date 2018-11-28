#include <bits/stdc++.h>
using namespace std;

int main(){
int t;
cin>>t;
for(int b=1; b<=t; b++){
    string n;
    cin>>n;

    int a[n.length()];

    for(int i=0; i<n.length(); i++)
        a[i] = (int)(n[i] - '0');

    for(int i=0; i<n.length()-1; i++){
        if(a[i+1] < a[i]){
            for(int j=i+1; j<n.length(); j++)
                a[j] = 9;

            a[i] -= 1;

            for(int k=i; k>0; k--){
                    if(a[k-1] > a[k]){
                        a[k-1] -=1;
                        a[k] = 9;
                    }
                    else{
                        break;
                    }
                }

         break;
        }
    }


    cout<<"Case #"<<b<<": ";
    for(int i=0; i<n.length(); i++){
        if(a[i] != 0)
            cout<<a[i];

    }

    cout<<endl;
}



}
