#include<bits/stdc++.h>
using namespace std;
int tc,n,f,tope,res;
vector<int>v;
string x;
bool checa() {
    bool flag=true;
    tope=v[0];
    for(int i=1;i<v.size();i++)
        if(v[i]<v[i-1]) {
            flag=false;
            break;
        }
    return flag;
}
int main(){
    freopen("i.in","r",stdin);
    freopen("o.out","w",stdout);
    scanf("%d",&tc);
    int t;
     t=1;
    while(tc--) {
        f=1;
        res=0;
        scanf("%d",&n);
        for(int i=n;i>=0;i--){
             v.clear();
            stringstream ss;
            ss << i;
            x = ss.str();
            for(int i=0;i<x.size();i++){
                v.push_back(x[i]-48);
            }
            if(checa()){
                res=i;
                f=0;
                break;
            }
        }
        printf("Case #%d: %d\n",t,res);
        t++;
    }
}
