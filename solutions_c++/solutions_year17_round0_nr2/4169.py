#include<bits/stdc++.h>

using namespace std;

bool isTidy(long n){
long prev=LONG_MAX; long next=0;long t;
while(n>0){
      t=n%10;
      next=t;
    if(next>prev)
        return false;

      n=n/10;
      prev=next;

}

return true;
}
long long power(long long n,int t){

long long temp=n;
    if(t==0)
        return 1;

for(int i=0;i<t-1;i++){
    n=n*temp;
}
return n;
}
int main(){
freopen("B-large.in","r",stdin);

freopen("B-large.out","w",stdout);
int t;
cin>>t;
long long a[t];

for(int i=0;i<t;i++){
    cin>>a[i];

}

long longtemp,divd;
for(int i=0;i<t;i++){
long long temp=a[i];long long prev=LONG_LONG_MAX; long long next=0;long long rem=0;
int count=-1;
while(temp!=0)
{
    divd=temp%10;
    next=divd;
    if(next>prev)
    {
        a[i]=a[i]-(rem+1);
        if(next==0)
        next=9;
        else
        next--;
        //cout<<a[i]<<" rembf "<<rem<<" "<<temp<<" count "<<count<<" next "<<next<<" ";

        rem=a[i] % power(10,count+1);
        temp=a[i]/power(10,count+1);
        //cout<<temp<<" rem "<<rem<<endl;


    }
    temp=temp/10;
     prev=next;
      count++;
    rem=rem+prev*power(10,count);

}
    cout<<"Case "<<"#"<<i+1<<": "<<a[i]<<endl;

}



}


