#include <iostream>
using namespace std;

#define MOD 1000000007

int main()
{
    long long int i,j,t,T;
    string str;
    cin>>T;
    for(t=1;t<=T;t++){
        int prev,marker=0,next;
        int l;
        cin>>str;
        l = str.length();
        prev = (int)str[0]-48;
        for(i=1;i<l;i++){
            int next = (int)str[i]-48;
            if(prev<next){
                prev = next;
                marker = i;
                continue;
            }
            else if(prev == next)continue;
            else{
                str[marker] = (char)(prev-1+48);
                for(j=marker+1;j<l;j++)str[j]='9';
                break;
            }
        }
        cout<<"Case #"<<t<<": ";
        int flag=0;
        for(i=0;i<l;i++){
            if(str[i]!='0')flag=1;
            if(flag!=0)cout<<str[i];
        }
        cout<<endl;
    }
    return 0;
}

