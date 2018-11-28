#include<iostream>
#include<cmath>
using namespace std;
int tidy(int);
int main(){
int t;
cin>>t;int co=1;
while(t>=co)
{
    int no;
    cin>>no;
    for(int i=no;i>=1;i--)
    {
        if(tidy(i)==1)
        {
            cout<<"Case #"<<co<<": "<<i<<endl;
            break;
        }
    }

co++;

}}
int tidy(int no)
{
    int i,tp=no;
    for(i=0;tp!=0;i++)
    {
        tp=tp/10;

    }
    int *mat=new int[i];
    int k=0,flg=1;
    while(no!=0)
    {
        mat[k++]=no%10;
        no=no/10;
    }
    for(k=0;k<i-1;k++)
    {
        if(mat[k]<mat[k+1])
            flg=0;
    }
    delete mat;
    return flg;
}
