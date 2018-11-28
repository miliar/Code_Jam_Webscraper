#include<iostream>
using namespace std;
string n;
int t;
long long res;
int main(){
    cin>>t;
    for(int tt=0;tt<t;tt++){
        cin>>n;
        bool over;
        do{
        over=false;
        for(int i=1;i<n.size();i++){
            if(over)
                n[i]='9';
            else
            if(n[i-1]>n[i]){
                n[i-1]--;
                over=true;
                n[i]='9';
            }
            
        }
       
        }while(over==true);
        long long res=0;
        for(int i=0;i<n.size();i++){
            res*=10LL;
            res+=(long long)(n[i]-'0');
        }
        cout<<"Case #"<<tt+1<<": ";
        cout<<res<<endl;
    }
}