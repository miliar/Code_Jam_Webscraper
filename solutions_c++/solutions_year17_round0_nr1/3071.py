#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void pjam(int tt){
    printf("Case #%d: ",tt);
}
string s;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,it;
    cin>>t;
    for(it=1;it<=t;it++){
        int i,j,k,flip=0;
        bool flag=true;
        cin>>s>>k;
        for(i=0;i<s.size()&&flag;i++){
            if(s[i]=='-'){
                if((int)s.size()-i<k)
                    flag=false;
                else{
                    flip++;
                    for(j=i;j-i<k;j++)
                        s[j]='+'+'-'-s[j];
                }
            }
        }
        pjam(it);
        if(flag)
            cout<<flip<<"\n";
        else
            cout<<"IMPOSSIBLE\n";
    }
}
