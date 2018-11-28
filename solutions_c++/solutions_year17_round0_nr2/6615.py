#include<bits/stdc++.h>
using namespace std;
stack <int>s;
int main(){
    freopen("blar.in","r",stdin);
    freopen("blarans.in","w",stdout);

int t,i,testcases;
scanf("%d",&t);
int ar[20];
unsigned long long int n,d;
for(testcases=1;testcases<=t;testcases++){
    scanf("%llu",&n);
    d=n;
    bool f=false;
    int i=0;
    while(d>0){
        ar[i++]=d%10;
        d/=10;
        //cout<<i;
    }
    i-=1;
    int ind=i;
    while(i>0){
        if(ar[i]>ar[i-1]){
            f=1;
            break;}
            i--;
    }
    if(!f)
    cout<<"Case #"<<testcases<<": "<<n<<"\n";
    else{
            int j=0;
          while(1){

            while(j<i){
               ar[j]=9;
               if(ar[j+1]!=0){
                ar[j+1]-=1;
                j=j+1;
               }
               else if(ar[j+1]==0){
                while(ar[j+1]==0){
                    ar[j]=9;
                    j=j+1;
                }
                ar[j]=9;
                ar[j+1]-=1;
                j=j+1;
               }
            }
f=false;
         i=ind;
    while(i>0){
        if(ar[i]>ar[i-1]){
            f=1;
            break;}
            i--;
    }
    if(!f)
        break;
}
    cout<<"Case #"<<testcases<<": ";
    for(i=0;i<=ind;i++)
        if(ar[i]!=0)
        s.push(ar[i]);

    while(!s.empty()){
        cout<<s.top();
        s.pop();
        }
    cout<<"\n";
    }
}

return 0;
}
