#include<vector>
#include<iostream>
using namespace std;
int main()
{
int test,size;
cin>>test;
int limit;
string s;
int k=0;
int a=1,j;
int count=0;
vector<string>v;
vector<int>l;
bool res=true;

k=1;
while(k<=test)
{


cin>>s;
cin.ignore();
cin>>limit;

res=true;
count=0;



size=s.length();
for(int i=0;i<size;i++)
{
if(s.at(i)=='+')
{


}
else
{

count++;
a=0;
j=i;
if(j+limit-1 <size)
{
j=i;
while(a<limit)
{
if(s.at(j)=='+')
{


s.at(j)='-';
}else
{

s.at(j)='+';


}
j++;
a++;

}

}
else
{
cout<<"Case #"<<k<<": IMPOSSIBLE\n";
res=false;
break;
}


}
}

if(res==true)
{
cout<<"Case #"<<k<<": "<<count<<"\n";
}
k++;
}

return 0;
}
