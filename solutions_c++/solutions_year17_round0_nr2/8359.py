
#include <iostream>

using namespace std;

void gen(int no[],int pos,int flag)
{
    if (pos>17) {
        return;
    }
    if (pos+1>=flag) {
        no[pos+1]=9;
    }
    if(no[pos]<=no[pos+1])
    {
        gen(no, pos+1,flag);
    
    }
    else
    {
        no[pos]--;
        no[pos+1]=9;
        flag=pos+1;
        gen(no, pos-1,flag);
    }
    
}
int main() {
    int t,c=0,k=18,i;
    long n;
    int di[19];
    cin>>t;
    
    while (t--)
    {
        c++;
        k=18;
        cin>>n;
        while (n) {
            di[k--]=n%10;
            n/=10;
        }
        di[k]=0;
        gen(di, k,19);
        while (di[k]==0 && k<18) {
            k++;
        }
        cout<<"\nCase #"<<c<<": ";
        for(i=k;i<19;i++)
            cout<<di[i];
        
        
    }
   
    return 0;
}
