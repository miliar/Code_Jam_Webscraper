#include <bits/stdc++.h>
using namespace std;
int T,cas=0;
bool able(int from,int to,char raw[]){
    char normal=raw[from];
    for(int i=from;i<to;i++){
        if(raw[i]<normal)return false;
        else if(raw[i]>normal)break;
    }return true;
}
int main(){
    //freopen("B2.in","r",stdin);
    //freopen("B2.out","w",stdout);
    scanf("%d",&T);
    while(T--){
        char raw[25];
        char out[25];
        cin>>raw;
        int len=strlen(raw);
        for(int i=0;i<len;i++){
            if(able(i,len,raw))out[i]=raw[i];
            else{
                out[i]=(char)(raw[i]-1);
                for(int j=i+1;j<len;j++)out[j]='9';
                break;
            }
        }
        cout<<"Case #"<<++cas<<": ";
        if(out[0]!='0')cout<<out[0];
        for(int i=1;i<len;i++){
            cout<<out[i];
        }cout<<endl;
}
}
