#include <bits/stdc++.h>
using namespace std;
const int maxn = 2333;
char t[maxn];
int T;

int main(){
    freopen("b.txt","w",stdout);
    std::cin>>T;
    int _case = 0;
    while(T--){
        cin>>t;
        int len = strlen(t);
        cout<<"Case #"<<++_case<<": ";
        for(int i=0;i<len;i++){
            if(t[i]>t[i+1] && i!=len-1){
                if(i!=0 && t[i]>=t[i-1]+1){
                    t[i]-=1;
                    for(int j=i+1;j<len;j++)t[j]='9';
                    for(int j=0;j<len;j++)cout<<t[j];cout<<endl;
                    break;
                }
                else if(i==0){
                    //cout<<"asdf"<<endl;
                    
                    if(t[i]!='1')cout<<(char)(t[i]-1);
                    //cout<<endl;
                    for(int j=1;j<len;j++)cout<<'9';cout<<endl;
                    break;
                }
                else {
                    int pos = i;
                    //cout<<"asdf"<<endl;
                    //cout<<t[pos]<<" "<<t[pos-1]<<endl;
                    while(pos && t[pos]==t[pos-1]) pos--;
                    //cout<<pos<<endl;
                    if(pos==0){
                        if(t[pos]!='1') cout<<(char)(t[pos]-1);
                        for(int j=1;j<len;j++) cout<<'9';
                        cout<<endl;
                        break;
                    }
                    else {
                        for(int j=0;j<pos;j++)cout<<t[j];
                        cout<<(char)(t[pos]-1);
                        for(int j=pos+1;j<len;j++)cout<<'9';cout<<endl;
                        break;
                    }
                }
            }
            if(i==len-1){
                for(int j=0;j<len;j++)cout<<t[j];
                cout<<endl;
            }
        }
    }
    return 0;
}
