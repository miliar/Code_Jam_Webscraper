// C++ program to print all n-digit numbers whose digits
// are strictly increasing from left to right
#include <bits/stdc++.h>
#define ll long long
#define pll pair<ll,ll>
#define lim 1000000000000000001
using namespace std;
int t,k;
string s;
//map<long long,bool> was;
long long solve(int i,string ch)
{
    if(i==0)return atoll(ch.c_str());
    k=atoi(ch.substr(i-1,1).c_str());
    if(k>atoi(ch.substr(i,1).c_str())){
        k=47+k;
        ch[i-1]=(char)k;
        for(int j=i;j<ch.length();j++)ch[j]='9';
    }
    return solve(i-1,ch);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cin>>s;
        cout<<"Case #"<<tt<<": "<<solve(s.length()-1,s)<<endl;
    }

    return 0;
}
