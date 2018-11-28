#include<iostream>
#include<cstring>
using namespace std;
int main()
{
long long int i,j,attem,temporary,o,n,no;
cin>>i;
no=1;
while(i--)
{
attem=0,temporary=0;
string b;
cin>>b;
cin>>o;
long long int l=b.length();
if (o<=0)
cout<<"Case #"<<no<<": "<<"IMPOSSIBLE"<<endl;
else
{
for(n=0;n<=(l-o);n++)
{
if(b[n]=='-')
{
b[n]='+';
for(j=n+1;j<n+o;j++)
{
if(b[j]=='-')
b[j]='+';
else if(b[j]=='+')
b[j]='-';
}
attem++;


}
}

for(n=0;n<l;n++)
{
if(b[n]=='-')
{
temporary=1;
break;
}
}
if(temporary==0)
{
cout<<"Case #"<<no<<": "<<attem<<endl;
}
else
cout<<"Case #"<<no<<": "<<"IMPOSSIBLE"<<endl;
}
no++;
}


return 0;
}