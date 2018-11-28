// Lavina Jain
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define INF 1e20
#define MAX 1000000007
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL);
#define cases int t; cin>>t; while(t--)

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

int main()
{
    int t,z,N,R,O,Y,G,B,V,i,a,b,c,rem;
    map<char,char> mp;
    bool pos;
    string s,s1;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        mp.clear();
        s="";
        pos=1;
        cin>>N>>R>>O>>Y>>G>>B>>V;
        a=max(R,max(B,Y));
        if(a==R)
        {
            b=B;    c=Y;
            mp['a']='R';
            mp['b']='B';
            mp['c']='Y';
        }
        else if(a==B)
        {
            b=R;    c=Y;
            mp['a']='B';
            mp['b']='R';
            mp['c']='Y';
        }
        else
        {
            b=R;    c=B;
            mp['a']='Y';
            mp['b']='R';
            mp['c']='B';
        }
        if(b+c<a)
        {
            pos=0;
        }
        for(i=0;i<a;i++)
        {
            s=s+mp['a'];
        }
        rem=0;
        int point=0;
        for(i=0;i<b;i++)
        {
            s1="";
            for(int j=0;j<=point;j++)
            {
                s1=s1+s[j];
            }
            s1=s1+mp['b'];
            for(int j=point+1;j<s.length();j++)
            {
                s1=s1+s[j];
            }
            point+=2;
            s=s1;
        }
        rem=a-b;
        for(i=0;i<rem;i++)
        {
            s1="";
            for(int j=0;j<=point;j++)
            {
                s1=s1+s[j];
            }
            s1=s1+mp['c'];
            for(int j=point+1;j<s.length();j++)
            {
                s1=s1+s[j];
            }
            point+=2;
            c--;
            s=s1;
        }
        point=1;
        for(i=0;i<c;i++)
        {
            s1="";
            for(int j=0;j<=point;j++)
            {
                s1=s1+s[j];
            }
            s1=s1+mp['c'];
            for(int j=point+1;j<s.length();j++)
            {
                s1=s1+s[j];
            }
            point+=3;
            s=s1;
        }
        cout<<"Case #"<<z<<": ";
        if(!pos)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<s<<endl;
        }
    }
    return 0;
}
