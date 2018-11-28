#include<bits/stdc++.h>
using namespace std;
int main()
{
int z1, t1;
cin>>t1;
for(z1=0;z1<t1;z1++)
{
std::priority_queue<int> a;
int b,c,d,e,i,f;
cin>>e;
a.push(e);
cin>>b;
for(i=0;i<b;i++)
{
f=a.top();
c=f/2;
d=(f-1)/2;
a.push(c);

a.push(d);

a.pop();
}

cout<<"Case #"<<z1+1<<":"<<" "<<c<<" "<<d<<"\n";   

}
}
