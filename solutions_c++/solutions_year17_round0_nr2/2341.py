#include<bits/stdc++.h>
using namespace std;
void fileMode(){
    freopen("input2.in","r",stdin);
    freopen("output_file_name1.out","w",stdout);
}
int main(){
    fileMode();
    int t,itr,len,l,tmp;
    string s;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>s;
        itr=0;
        while(!itr){
            len = s.length();
            tmp=0;
            for(int j=0;j<len-1;j++)
                if(s[j]>s[j+1]){
                    s[j]=s[j]-1;
                    for(int k=j+1;k<len;k++)
                        s[k]='9';
                }
            for(int j=0;j<len-1;j++)
                if(s[j]>s[j+1]){
                    tmp=1;
                    break;
                }
            if(tmp==0)
                itr=1;
        }
        l=s.length();
        int k;
        for(int j=0;j<l;j++)
            if(s[j]!='0'){
                k=j;break;
            }
        cout<<"Case #"<<i<<": ";
        for(int j=k;j<l;j++)
            cout<<s[j];
        cout<<"\n";
    }
}
