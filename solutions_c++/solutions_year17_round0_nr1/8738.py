

#include <iostream>
#include<string.h>
#include<stdio.h>
#include<cstdlib>
using namespace std;
struct arrays
{


    char arr[1000];
    int k;
};
 void flip(char &a)
{
    if(a=='+')
    {
        a='-';
    }
    else if(a=='-')
        a='+';
}


int main()
{
arrays a[1000];
int n,i,len,j,no,l;
cin>>n;
for(i=0;i<n;i++)
{
    scanf("%s",a[i].arr);
    cin>>a[i].k;
}i=0;
start:
for(i;i<n;i++)
{
    no=0;
    len=strlen(a[i].arr);
    for(j=0;j<=(len-a[i].k);j++)
    {
        if(a[i].arr[j]=='+')
            continue;
        else
        {
            for(l=0;l<a[i].k;l++)
            flip(a[i].arr[j+l]);

            no++;
        }
    }
    for(j=len-a[i].k;j<len;j++)
    {
        if(a[i].arr[j]=='-')
        {cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;i++;goto start;}
    }

    cout<<"Case #"<<i+1<<": "<<no<<endl;

}
}


