#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
string num;
bool check(string s){
    for(int i=0;i<s.size()-1;i++){
        if(s[i]>s[i+1])
            return false;
    }
    return true;
}

int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
    int t;
    cin>>t;
    int T=t;
    while(t--){
        cin>>num;
        cout<<"Case #"<<T-t<<": ";
        if(check(num)){
            cout<<num<<endl;
        }
        else{
            int pos=-1;
            for(int i=0;i<num.size()-1;i++){
                if(num[i]>num[i+1]){
                    pos=i;
                    break;
                }
            }
            int temp=pos;
            for(int i=pos;i>0;i--){
                if(num[i]==num[i-1])
                    temp=i-1;
            }
            num[temp]--;
            for(int i=temp+1;i<num.size();i++)
                num[i]='9';
            int flag=0;
            for(int i=0;i<num.size();i++){
                if(num[i]!='0'){
                    flag=1;
                    cout<<num[i];
                }
                else if(flag){
                    cout<<num[i];
                }
            }
            cout<<endl;
        }
    }

    return 0;
}
