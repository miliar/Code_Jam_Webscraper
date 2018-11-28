#include <bits/stdc++.h>

#include<iomanip>

using namespace std;

int main() {
int t,n,te=0;

cin>>t;
double d;

while(te<t)
{

cin>>d>>n;

int i;
double k[n],s[n],t[n],minPos,speed;

for(i=0;i<n;i++)
{
cin>>k[i]>>s[i];
double distance=(d-k[i]);
t[i]=distance/s[i];
}
minPos=*max_element(t,t+n);

speed=d/minPos;
cout<<fixed;
cout<<"Case #"<<te+1<<": ";cout<<setprecision(6)<<speed<<"\n";
te++;
}
return 0;

}
