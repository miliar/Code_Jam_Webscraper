#include <bits/stdc++.h>
#define lli long long int
#define vi vector <int>
using namespace std;

int displayvi(vi a){for(int i=0;i<a.size();i++) cout<<a[i]<<"-"; cout<<endl;}

/*int compare(string s1, string s2)
{
    
    if(s1.size()>s2.size()) return 1;
    if(s1.size()<s2.size()) return -1;
    //if(s1.size()==0) return 0;

    for(int i=0;i<s1.size();i++)
    {
        if(s1[i] > s2[i]) return 1;
        if(s1[i] < s2[i]) return -1;
    }
    return 0;
}

string nines(int i)
{
    string s="";
    while(i--) s=s+"9";
    return s;
}

string trim(string s)
{
    if(s.size>1 && s[0]='0') return s.substr(1);
    return s;
}

string max(string s1, string s2){s1=trim(s1);s2=trim(s2);if(compare(s1,s2)>=0) return s1; return s2;}

int tidy(string s)
{
    s=trim(s); char c= s[0]; for(int i=0;i<s.size()i++) {if(s[i]<c) return -1; c=s[i];} return 1;
}

string q2(string s)
{
    int l=s2.size();
    if(l==1 || tidy(s)) return trim(s);
    
    ans=nines(l-1);
    
    for(int i=0;i<n;i++)
    {
        
    }
    
    return ans;
}*/

int tidy(lli a)
{
    if(a<0) return 0;
    int r=a%10;
    while(a>0)
    {
        if(a%10 > r) return 0;
        r=a%10; a=a/10;
    }
    return 1;
}

lli nines(int i)
{
    //cout<<i<<endl;
    lli r=0;
    while(i--) r=r*10+9;
    return r;
}

int powerten(lli i)
{
    int p=0;
    while(i>0){p++;i=i/10;}
    return p;
}

lli ten(int i)
{
    return pow(10,i);
}

lli q22(lli s)
{
    lli ans;
    if(tidy(s)) return s;
    int p=powerten(s);    
    
    ans= nines(p-1);
    
    for(int i=1;i<p;i++)
    {
        lli pt=nines(i)+1;
        //cout<<pt;
        lli s1=s%pt;
        lli s2=s/pt;
        lli ans2=((s2-1)*pt)+nines(i);
        //cout<<s1<<"\t"<<s2<<"\t"<<ans2<<endl;
        
        if(tidy(s2-1)) {
            
            ans=max(ans,ans2);
        }
        
    }
    return ans;
}

int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        lli s; int k;
        cin>>s;
        //cin>>k;

        lli a=q22(s);
        cout<<"Case #"<<tt<<": "<<a<<endl;
    }
    // your code goes here
    return 0;
}
