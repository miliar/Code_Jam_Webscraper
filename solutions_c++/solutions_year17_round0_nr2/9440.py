#include<iostream>
#include<string>
#include<conio.h>
#include<stdio.h>
using namespace std;

int main()
{
freopen("P2S.in","r",stdin);
freopen("output_s1.out","w",stdout);
int t,l,k;

cin>>t;

int arr[18];//={0,1,2,3,4,5,6,7,8,9};

for(int i=1;i<=t;i++)
{
    int len;
    string s;
cin>>s;
int m=0;

len=s.length();
if(len==1)
{
cout<<"Case #"<<i<<": "<<s<<endl;
continue;
}
int j;
for(j=0;j<s.length();j++)
    arr[j]=s[j]-48;


for(j=0;;j++)
{
    int f=0;
    l=len-1;
    for(k=len-1;k>0+m;k--)
    {
        if(arr[k]<arr[k-1])
            {f=1;
        break;
        }
    }


    if(f==0)
    {
        cout<<"Case #"<<i<<": ";
       if(arr[m]==0)m++;
        for(int x=m;x<len;x++)
            {cout<<arr[x];}
        cout<<endl;
    break;
    }

if(arr[l]==0)
 while(arr[l]==0&&l>0)
{
    //arr[l]
arr[l]=9;
--l;
if(arr[l]==0)arr[l]=1;
arr[l]--;

}
else
    arr[l]--;

if(arr[m]==0)
{
 m++;
}

}//j
}//i
    return 0;
}
