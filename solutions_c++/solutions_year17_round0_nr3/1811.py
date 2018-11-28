#include <iostream>
#include <map>
using namespace std;
typedef long long LL;

int main()
{
int t,T;

cin>> T;
t=T;
LL n,k;
map<LL,LL> stat;

while(T--)
{
	cout <<"Case #"<<t-T<<": ";	
cin>>n>>k;
stat.clear();
stat[n]=1;

while(k)
{
LL i=stat.rbegin()->first;
if(stat[i]>=k) break;
stat[i/2]+=stat[i];
stat[i-i/2-1]+=stat[i];	
k-=stat[i];
stat.erase(i);	
}
LL tmp=stat.rbegin()->first;
cout << tmp/2<<" "<<tmp-tmp/2-1; 
if(T) cout<<endl; 
}
}
