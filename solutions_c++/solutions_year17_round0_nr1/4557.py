#include <iostream>
using namespace std ;

int main ()
{
    int a[1005],n,x,y,i,j,flag,l,k,t;
    char str[1005];
    cin>>t;
    for(k=1;k<=t;k++){
        cin>>str>>n;
        for(i=0;str[i]!='\0';i++){
            if(str[i]=='+')
                a[i]=0;
            else
                a[i]=1;
        }
        l=i;
        flag=0;
        x=0;
        for(i=0;i<l-n+1;i++)
        {
            if(a[i]==1){
                for(j=i;j<i+n;j++)
                    if(a[j]==0) a[j]=1;
                    else a[j]=0;
                x++;
            }
        }
        for(i=l-n+1;i<l;i++)
                if(a[i]==1){
                    flag=1;break;
                }

        if(flag==1) cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<k<<": "<<x<<endl;

    }

}
