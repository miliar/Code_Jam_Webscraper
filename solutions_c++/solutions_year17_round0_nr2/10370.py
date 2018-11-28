#include<iostream>
#include<stdio.h>
#include<string>
#include<sstream>
using namespace std;
int main()
{freopen("B-small-attempt0.in", "r", stdin);
    freopen("1-out.txt", "w", stdout);

unsigned long long int t,k,p,i,alpha,j,num;
string str;
char *ptr=NULL;
cin>>t;
int flag=1;
for(i=1;i<=t;i++)
{
cout<<"Case #"<<i<<": ";
flag=1;
cin>>num;
//cout<<num<<endl;
ostringstream convert;
convert<<num;
str=convert.str();


while(flag==1)
{
int flag2=1;
int flag3=0;
if(str.size()>3)
{flag3=1;
for(k=0;k<str.size()-1;k++)
{
if(str[k]<str[k+1])
{flag3=0;
break;
}
}
}
if(flag3==1)
{
flag=0;

alpha=str[0]-'0';
if(alpha!=1)
{
cout<<alpha-1;
}
for(p=0;p<str.size()-1;p++)
{cout<<"9";
}
}
else{

for(j=0;j<str.size()-1;j++)
{
//cout<<str<<" ";
//cout<<str[j]<<endl;
if(int(str[j])>int(str[j+1]))
{flag2=0;
break;
}

}
if(flag2==0)
{
flag=1;
num=num-1;
//cout<<"new num is "<<num<<endl;
convert.str("");
convert<<num;
str=convert.str();
//cout<<"new str is"<<str<<endl;
}
else{
flag=0;
cout<<num;
}



}



}

cout<<endl;
}






return 0;
}
