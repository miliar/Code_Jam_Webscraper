#include <iostream>
#include <string>
#include <cmath>
using namespace std;

long long test(long long n)
{
    string s=to_string(n);
    int i,j,fl=1;
    while(fl==1){
    fl=0;
    for(i=1;i<s.size();i++)if(s[i]<s[i-1])
    {
        s[i-1]=s[i-1]-1;
        for(j=i;j<s.size();j++)s[j]='9';
        fl=1;
        break;
    }
    }
    //cout<<s<<endl;
    return stoll(s,NULL,10);
}

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        cout<<"Case #"<<tci<<": ";
        long long n;
        cin>>n;
        cout<<test(n)<<endl;
    }
    return 0;
}
