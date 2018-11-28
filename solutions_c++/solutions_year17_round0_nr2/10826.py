#include<iostream>
using namespace std;
int isTidy(int x){

    while(x){
        if(x%10 >= (x/10)%10){
            x=x/10;
        }
        else
            break;
    }
    if(x==0)
        return 1;
    else
        return 0;
}

int main(){
    int t,ans;
    cin>>t;
    for(int j=1;j<=t;j++){

        int n;
        cin>>n;
        for(int i=n;i>=1;i--){
            if(isTidy(n)){
                 ans = n;
                break;
            }
            n--;
            //cout<<"s";
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;

    }

    return 0;
}
