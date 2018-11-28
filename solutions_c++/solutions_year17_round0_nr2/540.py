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
string tostr1(long long n)
{
    string a="";
    while(n!=0)
    {
        a+='0'+n%10;
        n/=10;
    }
    string b="";
    for(int i=a.length()-1;i>=0;i--)
        b+=a[i];
   // cout<<b<<endl;
    return b;
}
string remove_zero(string s)
{
    bool z=false,z1=false;
    string a="";
    int chng=(int)s.length();
    for(int i=(int)s.length()-1;i>=0;i--)
    {
        if(s[i]=='0')
            z=true;
        if(s[i]=='1' && z)
        { z1=true; z=false;}
        
        if(s[i]=='1' && z1)
           z1=true;
        
        if(s[i]>'1' && z)
        { chng=i; z=false;}
        
        if(s[i]>'1' && z1)
        { chng=i;z1=false;}
        
    }
    if(z1)
        chng=0;
    
    for(int i=0;i<s.length();i++)
    {
        if(i<chng)
            a+=s[i];
        else if (i==chng)
            a+=s[i]-1;
        else if(i>chng)
            a+='9';
    }
    
  //  cout<<a<<endl;
    return a;
}
string inc_no(string s)
{
    string a=s;
    int j;
    bool b=false;
    
    for(int i=1;i<s.length();i++)
    {
        if(b)
            a[i]='9';
        else if(a[i-1]>a[i])
        {
            j=i-1;
            while(j>0 && a[j]==a[j-1])
                j--;
            
            a[j]--;
            //a[i]='9';
            i=j;
            b=true;
        }
    }
    return a;
}
string strip(string s)
{
    string a="";
    int i=0;
    while(s[i]=='0')
        i++;
    while(i<s.length())
        a+=s[i++];
    return a;
}
bool cond(long long n)
{
    int t,p=n%10;
    n=n/10;
    while(n!=0)
    {
        t=n%10;
        if(p<t)
            return false;
        p=t;
        n=n/10;
    }
    return true;
}
long long brute(long long n)
{
    n++;
    while(n--)
    {
        if(cond(n))
            return n;
    }
    return 0;
}
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,cc=1;
    long long n,temp;
    infile>>t;
    string s;
    while(t--)
    {
        infile>>n;
        s=tostr1(n);
        s=remove_zero(s);
        s=inc_no(s);
        s=strip(s);
      //  cout<<"ans : "<<s<<endl;
        outfile<<"Case #"<<cc++<<": "<<s<<endl;
    //    temp=brute(n);
      //  if(tostr1(temp)!=s)
        // cout<<n<<" : "<<temp<<" "<<s<<endl;
            
        

        
    }
    outfile.close();
    infile.close();

    return 0;
}