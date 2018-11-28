#include<iostream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int ab;

void checkl(int i)
{
vector<int> vi;
int f,r,t,vii,c=0;
t=i;
while(t)
{
     r=t%10;
     t=t/10;
     c=c+1;
     vi.push_back(r);
}

for(vii=1;vii<c;vii++)
{
    if(vi[vii-1]>=vi[vii])
    f=1;
    else
    goto lln;
}
ab=i;
lln:   ;
}
int main()
{
     freopen("B-small-attempt2.in","r",stdin);
     freopen("output.out","w",stdout);
    int i,t,it,x,nj,j;
    vector<int> n;
    cin>>t;
    for(it=0;it<t && it<101;it++){
    cin>>x;
    n.push_back(x);
    }
    for(j=0;j<t;j++){
        nj=n[j];
    for(i=1;i<=nj && i<1001;i++)
    {
 checkl(i);
    }
    cout<<"case #"<<(j+1)<<": ";
    cout<<ab<<endl;
    }
    return 0;
}