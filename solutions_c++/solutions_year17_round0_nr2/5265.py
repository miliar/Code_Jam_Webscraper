#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,p=1;
    cin>>t;
    while(t--){
    string n;
        cin>>n;
        unsigned long long len=n.length();
        unsigned long long x,y,loc,flag=0;
        for(unsigned long long i=0;i<len-1;i++ ){
            x=n[i];
            y=n[i+1];
            if(x>y){
                flag=1;
                loc=i;
                break;
            }
        }
        if(flag==1){
            y=n[loc];
            if(y==49){
                for(unsigned long long i=0;i<len-1;i++)
                    n[i]='9';
                cout<<"Case #"<<p++<<": ";
                for(unsigned long long i=0;i<len-1;i++){
                    cout<<n[i];
                }
                cout<<endl;
            }
            else{
                while(loc>0&&n[loc]==n[loc - 1]){
                    loc--;
                }
                n[loc]=(char)(--y);
                for(unsigned long long i=loc+1;i<len;i++){
                    n[i]='9';
                }
                cout<<"Case #"<<p++<<": "<<n<<endl;
            }
        }
        else{
            cout<<"Case #"<<p++<<": "<<n<<endl;
        }
    }
    return 0;
}
