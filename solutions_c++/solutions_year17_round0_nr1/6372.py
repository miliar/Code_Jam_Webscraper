#include <iostream>
using namespace std;

#define MOD 1000000007

int main()
{
    long long int i,t,T;
    string str;
    cin>>T;
    for(t=1;t<=T;t++){
        int count =0,ans=0,next_val=-1;
        int k,l;
        cin>>str;
        cin>>k;
        l = str.length();
        for(i=0;i<l;i++){
            int f=0;
            if(str[i]=='-'){
                str[i]='+';
                f=1;
                count++;
            }
            if(count!=0 && str[i]=='+' && f==0){
                str[i]='-';
                count++;
                if(next_val==-1)next_val=i;
            }
            if(count == k ){
                if(next_val!=-1)i = next_val-1;
                next_val=-1;
                ans++;
                count =0;
            }
        }
        if(count!=0)cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}

