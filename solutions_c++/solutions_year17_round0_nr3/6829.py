#include<iostream>
#include<stdio.h>
using namespace std;
bool A[1024];
int k,m,R,L, a, b;
int sloji()
{
    int l[1024];
    int r[1024];
    for(int i=0;i<=m;i++)
    {
        l[i]=-1;
        r[i]=-1;
    }
    int ll=1, lr=m, index=-1, maxx=-1, MM=-1;
    for(int i=m-1;i>=0;i--)
    {
        if(A[i]==0)
        {
            r[i]=lr-i;
        }
        else
        {
            lr=i;
        }
    }
     for(int i=2;i<=m;i++)
    {
        if(A[i]==0)
        {
            l[i]=i-ll;
            if(min(r[i],l[i])>maxx)
            {
                maxx=min(r[i], l[i]);
                MM=max(r[i],l[i]);
                index=i;
                L=l[i];
                R=r[i];
            }
            else if(min(r[i],l[i])==maxx)
            {
                if(max(r[i],l[i])>MM)
                {
                    MM=max(r[i],l[i]);
                    index=i;
                    L=l[i];
                    R=r[i];
                }
            }

        }
        else
        {
            ll=i;
        }
    }
    A[index]=1;
   /* cout<<"m "<<m<<endl;
    for(int i=1;i<=m;i++)
        cout<<l[i]<<" ";
    cout<<endl;
    for(int i=1;i<=m;i++)
        cout<<r[i]<<" ";
    cout<<endl;
   /* cout<<"blq:";
    for(int i=1;i<k;i++)
        cout<<A[i];
    cout<<endl;*/
    //cout<<l[index]<<" "<<r[index];
    ///cout<<L-1<<" "<<R-1<<endl;
    return index;
}
int main(){
cin.tie(0);
ios::sync_with_stdio(false);
freopen("codeJam3.in","r",stdin);
freopen("codeJam3.out","w",stdout);
int n;
cin>>n;
for(int i=0;i<n;i++)
{
    cin>>m>>k;
    m+=2;
    for(int j=0;j<=m;j++)
        A[j]=0;
    A[1]=1;
    A[m]=1;
    for(int j=0;j<k;j++)
    {
        sloji();
    }
   /* for(int j=1;j<=m;j++)
        cout<<A[j];
    cout<<endl;*/
    cout<<"Case #"<<i+1<<": "<<max(L,R)-1<<" "<<min(L,R)-1<<endl;

}



return 0;
}
