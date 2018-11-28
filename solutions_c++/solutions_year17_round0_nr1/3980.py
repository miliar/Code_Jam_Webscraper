#include "bits/stdc++.h"
using namespace std;
int test,countx,k;
string d;
bool check;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&test);
    for(int l=1;l<=test;l++){
        cin>>d>>k,countx=0,check=false;
        for(int i=0;i<=d.length()-k;i++){
            if(d[i]=='-'){
                for(int j=0;j<k;j++) d[i+j]=((d[i+j]=='+')? '-':'+');
                countx++;
            }
        }
        for(int i=d.length()-k+1;i<d.length();i++){
            if(d[i]=='-'){
                printf("Case #%d: IMPOSSIBLE\n",l),check=true; break;
            }
        }
        if(!check) printf("Case #%d: %d\n",l,countx);
    }
}
