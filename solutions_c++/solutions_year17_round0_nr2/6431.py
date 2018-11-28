#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ite iterator
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define null NULL
#define ioS ios::sync_with_stdio(false);
#define mod 1000000007
#define Max 9000000000000000000
#define Min (-1)*9000000000000000000


int main()
{
ioS;
ll i,j,k,l,r,m,n,o,t;

cin>>t;
char str[25];
for(o=1;o<=t;o++)
{
cin>>str;
l=strlen(str);
bool flag=1;
for(i=1;i<l;i++)
{
    if(str[i]<str[i-1])
        flag=0;
}
if(flag)
{
    cout<<"Case #"<<o<<": ";
    cout<<str<<endl;
    continue;
}
m=0;
for(i=0;i<l-1;i++)
{
    if(str[i]>str[i+1])
    {
       while(m!=0&&str[m]==str[m-1])
        m--;
       break;
    }
    else
    {
        m++;
    }

}


cout<<"Case #"<<o<<": ";

for(i=0;i<l;i++)
{
    if(i<m)
        cout<<str[i]-'0';
    else if(i==m)
        {
            if(i==0&&str[i]=='1')
                continue;
            cout<<str[i]-'0'-1;
        }
    else
        cout<<'9';
}

cout<<endl;

}
}
