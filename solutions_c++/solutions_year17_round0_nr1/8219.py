#include <iostream>
#include<cstdio>
#define lld long long int
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        string s;
        bool flag=true;
        int k,temp=0,minUses=0,next_j=0;
        cin>>s>>k;
        for(int j=0;j<=s.length()-k;j++){
            next_j=j;
            if(temp==0){
                j=next_j;
            }

            if(s[j]=='-'){
                temp=k;
                minUses++;
                //cout<<minUses<<endl;
            }
            //cout<<"H"<<endl;
            //cout<<s<<endl;
            while(temp){
                if(s[j+temp-1]=='-'){
                    s[j+temp-1]='+';
                }
                else{
                    s[j+temp-1]='-';
                    next_j=j;
                }
                temp--;
                //cout<<"INSIDE"<<endl;
            }
        }
        for(int j=0;j<s.length();j++){
            if(s[j]=='-'){
                flag=false;
                break;
            }
        }
        if(flag){
            cout<<"Case #"<<(i+1)<<": "<<minUses<<endl;
        }
        else{
            cout<<"Case #"<<(i+1)<<": IMPOSSIBLE"<<endl;
        }
    }
return 0;
}
