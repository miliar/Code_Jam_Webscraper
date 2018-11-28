#include<iostream>
#include<string>
using namespace std;
int main(){
    int t,k;
    string s;
    cin>>t;
    for(int i=1;i<=t;i++){
        int q=0,b=0;
        cin>>s>>k;
        int n=s.size();
        for(int j=0;j<=(n-k);j++){
            if(s[j]=='-'){
                q++;
                for(int m=j;m<j+k;m++){
                    if(s[m]=='-'){
                        s[m]='+';
                    }
                    else
                        s[m]='-';
                }
            }
        }
        for(int a=0;a<n;a++){
            if(s[a]=='-'){
                b=1;
                break;
            }
        }
        if(b==1){
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<i<<": "<<q<<endl;
        }
    }
return 0;
}
