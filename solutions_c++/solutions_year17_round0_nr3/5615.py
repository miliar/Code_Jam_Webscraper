#include<bits/stdc++.h>
using namespace std;
int main()
{int z,t;
cin>>t;
for(z=0;z<t;z++)
{ std::priority_queue<int> a;
int b,c,d,e,i,f;
cin>>e;
a.push(e);
cin>>b;
for(i=0;i<b;i++)
{f=a.top();
    c=f/2;
d=(f-1)/2;
a.push(c);
a.push(d);
a.pop();
}
 cout<<"Case #"<<z+1<<":"<<" "<<c<<" "<<d<<"\n";   

}
return 0;
}