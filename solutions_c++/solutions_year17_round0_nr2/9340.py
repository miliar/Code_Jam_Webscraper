#include<bits/stdc++.h>
#include<fstream>
#define ll long long
using namespace std;





string setnines(string x,ll i){

for(ll j=i;j<x.length();j++){
        x[j] = '9';
}
return x;
}


int main(){

freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);


ll t;
cin>>t;

for(int k=1;k<=t;k++){

    string input;
    cin>>input;
    for(ll i=input.length()-1;i>=1;i--){
        if(input[i]>=input[i-1])
            continue;

        else{
            //cout<<input[i]<<" "<<input[i-1]<<endl;
            input[i-1]=input[i-1]-1;
            input = setnines(input, i);
            //cout<<input<<endl;
        }
    }

    ll x=0;

    while(input[x]=='0')
        input.erase(x,1);

cout<<"Case #"<<k<<": "<<input<<endl;
}

return 0;
}

