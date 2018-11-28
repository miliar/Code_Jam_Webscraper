#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++){
         char a[19];
         int j,k,m;
         cin>>a;
         j=strlen(a);
        if(j==1)
            cout<<"Case #"<<i<<": "<<a;
        else{
        j--;
        k=0;
        while(k!=j){
        for(k=0;k<j;k++){
            if(a[k]>a[k+1])
            {
                a[k]=(char)((int)a[k]-1);
                for(m=k+1;m<=j;m++)
                    a[m]='9';
                break;
            }
        }
    }
    cout<<"Case #"<<i<<": ";
    if(a[0]=='0')
        for(k=1;k<=j;k++)
            cout<<a[k];
    else
        for(k=0;k<=j;k++)
            cout<<a[k];
        }
    cout<<endl;
    }
    return 0;
}

