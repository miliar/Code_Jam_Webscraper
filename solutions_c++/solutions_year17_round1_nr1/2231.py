#include <iostream>

using namespace std;
char a[30][30];
int t,r,c;
int main()
{
cin>>t;
char ch;
int e,f;
for(int i=0;i<t;i++)
{
cin>>r;
cin>>c;
for(int p=0;p<r;p++)
{
for(int q=0;q<c;q++)
{
    cin>>a[p][q];
}
}

for(int p=0;p<r;p++)
{
for(int q=0;q<c;q++)
{
if(a[p][q]=='?')
{
continue;
}
else
{
ch=a[p][q];
e=q-1;
f=q+1;
while(a[p][e]=='?')
{
a[p][e]=ch;
e--;
}
while(a[p][f]=='?')
{
a[p][f]=ch;
f++;
}
}
}
}

for(int p=0;p<c;p++)
{
for(int q=0;q<r;q++)
{
if(a[q][p]=='?')
{
continue;
}
else
{
ch=a[q][p];
e=q-1;
f=q+1;
while(a[e][p]=='?')
{
a[e][p]=ch;
e--;
}
while(a[f][p]=='?')
{
a[f][p]=ch;
f++;
}
}
}
}

cout<<"Case #"<<i+1<<":"<<"\n";
for(int p=0;p<r;p++)
{
    for(int q=0;q<c;q++)
        cout<<a[p][q];
        cout<<"\n";
}

}
return 0;
}
