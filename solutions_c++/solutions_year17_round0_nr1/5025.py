#include<iostream>
using namespace std;
bool tab[1001];
bool swith[2001];
string data;
bool sw;
int k,t;
int main(){
    cin>>t;
    for(int tt=0;tt<t;tt++){
        sw=false;
        bool impossible=false;
        int res=0;
        cin>>data>>k;
        for(int i=0;i<data.size();i++){
            tab[i]=(data[i]=='+');
            swith[i]=0;
        }
        for(int i=0;i<data.size();i++){
            sw^=swith[i];
            if((tab[i]^sw)==0){
                //cout<<i<<" "<<tab[i]<<" "<<sw<<endl;
                sw=!sw;
                res++;
                swith[i+k]=1;
                if(i+k>data.size()){
                    impossible=true;
                }
            }
            
        }
        cout<<"Case #"<<tt+1<<": ";
        if(impossible)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<res<<endl;
    }
}