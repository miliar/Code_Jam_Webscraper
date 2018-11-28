#include<iostream>
#include<stdio.h>
using namespace std;
string blq(string a)
{
    a='0'+a;
    long long fail=-1;
    for(long long i=1;i<a.size();i++)
    {
        if(a[i]<a[i-1])
        {
            fail=i;
            break;
        }
    }
    if(fail==-1)
    {
        a.erase(0,1);
        return a;
    }
    for(long long  i=fail-1;i>0;i--)
    {
        if(a[i]-1>=a[i-1])
        {
            a[i]--;
            for(long long  j=i+1;j<a.size();j++)
                a[j]='9';
            break;
        }
    }
    while(a[0]=='0')
        a.erase(0,1);
    return a;
}
int main(){
cin.tie(0);
ios::sync_with_stdio(false);
freopen("codeJam2.in","r",stdin);
freopen("codeJam2.out","w",stdout);
long long n;
cin>>n;
for(long long i=0;i<n;i++)
{
    string a;
    cin>>a;
    cout<<"Case #"<<i+1<<": "<<blq(a)<<endl;
}

return 0;
}
