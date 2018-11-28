#include<iostream>
#include<vector>
using namespace std;



bool calculate(long int no)
{
vector<int>v;
long int n;
int r,len;
bool res;
res=true;
n=no;
v.erase(v.begin(),v.end());
while(n!=0)
{

r=n%10;
v.push_back(r);
n=n/10;
}
res=true;
len=v.size();
for(int i=0;i+1<len;i++)
{
if(v[i]>=v[i+1])
{
res=true;
}
else
{
res=false;
break;
}
}
return res;
}




int main()
{


int test;
long int no;
bool result=true;
cin>>test;
int t=1;

while(t<=test)
{

cin>>no;
result=calculate(no);



if(result==true)
cout<<"Case #"<<t<<": "<<no<<"\n";
else
{
while(true)
{
no--;
result=calculate(no);
if(result==true)
{
cout<<"Case #"<<t<<": "<<no<<"\n";
break;

}
else
{
    
}
}
}
t++;
}


return 0;
}










