#include<bits/stdc++.h>
#define r0 return 0
using namespace std;
int t,k;
string s;
int main(){
    fstream file;
  	file.open("pan.txt",ios::out);
    cin>>t;
    int i;
    for(i=1;i<=t;i++){
            getchar();
        cin>>s>>k;
        int j,l,c=0,f=0;
        for(j=0;j<s.size();){
            if(s[j]=='-'){
                    c++;
                for(l=j;l<=j+k-1;l++){
                    if(l==s.size()){
                        f=1;
                        break;
                    }
                    if(s[l]=='+')s[l]='-';
                    else s[l]='+';
                }
                if(l==j+k){
                j++;}
                else{
                    break;
                }
            }
            else{
                j++;
            }
        }
        if(f==0){
            file<<"Case #"<<i<<":"<<" "<<c<<endl;
        }
        else file<<"Case #"<<i<<":"<<" "<<"IMPOSSIBLE"<<endl;
    }
    r0;
}
