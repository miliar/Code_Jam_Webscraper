#include <iostream>
using namespace std ;

int main ()
{
    int p[100],r,i,j,flag,l,k=1,t,flip;
    char pc[1000];
    cin>>t;
    while(t--){
        cin>>pc;
        cin>>flip;
        for(i=0;pc[i]!=NULL;i++){
            if(pc[i]=='+')
                p[i]=1;
            else
                p[i]=0;
        }
        l=i;
        flag=0;
        r=0;
        for(i=0;i<l-flip+1;i++)
        {
            if(p[i]==0){
                for(j=i;j<i+flip;j++)
                    if(p[j]==1) p[j]=0;
                    else p[j]=1;
                r++;
            }
        }
        for(i=l-flip+1;i<l;i++)
                if(p[i]==0){
                    flag=1;
                    break;
                }

        if(flag==1)
            cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<k<<": "<<r<<endl;
        k++;

    }

}
