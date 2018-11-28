#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("out113.txt");
int main()
{
int t;
fin>>t;
int l;
l=1;
while(t--)
{
int flag=0;
string s;
fin>>s;
int k;
fin>>k;
int count1=0;
int l1=s.length();
for(int i=0;i<l1;i++)
{
if(s[i]=='-')
{
count1++;
if((i+k)>l1)
{
//fout<<i<<endl;
flag=1;
break;

}
for(int j=i;j<(i+k);j++)
{
if(s[j]=='-')
s[j]='+';
else
s[j]='-';
}

}
}
fout<<"Case #"<<l<<": ";
l++;
if(flag==1)
fout<<"IMPOSSIBLE"<<endl;
else
fout<<count1<<endl;
}
}
