#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mk make_pair
#define F first
#define S second

#define MOD (1000000007)
//#define max(a,b) ((a)>(b)?:(a):(b))
using namespace std;
int p[1005];
int ans(string s,int k)
{
    int a=0;
    int i=0,sum=0;
    memset(p,0,sizeof p);
    for(i=0;i<s.length()-k;i++)
    {
        sum+=p[i];
         if(sum%2==0 && s[i]=='+')
             continue;
         if(sum%2==1 && s[i]=='-')
             continue;
        sum+=1;
        p[i+k]++;
        cout<<i+k<<endl;
        a++;
    }
    bool b1=true,b2=true;
    int temp=sum;
    for(i=(int)s.length()-k;i<s.length();i++)
    {
        sum+=p[i];
        cout<<"i sum s[i] ="<<i<<" "<<sum<<" "<<s[i]<<" "<<b1<<endl;
        if(sum%2==0 && s[i]=='+')
         continue;
        if(sum%2==1 && s[i]=='-')
        continue;
        b1=false;
        
    }
    cout<<endl;
  //  i=s.length()-k;
    sum=temp;
    for(i=(int)s.length()-k;i<s.length();i++)
    {
        sum+=p[i];
        cout<<"i sum s[i] ="<<i<<" "<<sum<<" "<<s[i]<<" "<<b2<<endl;
        if(sum%2==0 && s[i]=='-')
          continue;
        if(sum%2==1 && s[i]=='+')
        { printf("here\n"); continue;}
        b2=false;
        
    }
    cout<<b1<<" "<<b2<<endl;
    if((!b1) && (!b2))
        return 2000;
    if((!b1) && b2)
        a+=1;
    cout<<a<<endl;
    return a;
        
}
string rev(string s)
{
    string a="";
    for(int i=s.length()-1;i>=0;i--)
        a+=s[i];
    return a;
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,k,c=1,temp;
    string s,s2;
    infile>>t;
    while(t--)
    {
        infile>>s>>k;
        cout<<s<<" "<<k<<endl;
        temp=ans(s,k);
        s2=rev(s);
        cout<<s2<<endl;
        temp = min(temp,ans(s2,k));
        if(temp<2000)
            outfile<<"Case #"<<c<<": "<<temp<<endl;
        else
            outfile<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
        c++;
    }
    outfile.close();
    infile.close();

    return 0;
}