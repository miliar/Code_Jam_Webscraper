#include<bits/stdc++.h>// <3 Nandini <3
using namespace std;
#define gc getchar
#define mp make_pair
#define pb push_back
#define sc scanint
#define dc print_int
#define f first
#define s second
#define ret return 0;
#define rf std::ios::sync_with_stdio(false);
#define mi 1000000007
#define tl int t;sc(t);while(t--)
#define vin vi arr; for(int i=0;i<n;i++){int a;sc(a);arr.pb(a);}
#define st string s1; getline(cin>>ws,s1);
#define sorta sort(arr.begin(),arr.end());
#define reva reverse(arr.begin(),arr.end());
#define pf(a) printf("%d",a);
#define mina *min_element(arr.begin(),arr.end())
#define maxa *max_element(arr.begin(),arr.end())
#define sl scanlong
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;
typedef long long int ll;
typedef pair<int, int> pii;
typedef unsigned long long int ull;


void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
void scanlong(ull &x);
void scanlong(ull &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
int main()
{
    int man,test;
    sc(test);
    man=test;
    while(test--)
    {
        string s1;
        int fo=0,go=0,ko;
        int co=0,jo=0;
        cin>>s1>>ko;
        int l = s1.size();
        for(int in=0;in<l;in++)
        {
        if(s1[in]=='-')
            {
                fo=1;
            break;
            }
        }

        if(fo==0)
        {cout<<"Case #";
        cout<<man-test<<": ";
        cout<<0<<endl;}
        else
        {
        for(int i=0;i<l;i++)
            {
            if(s1[i]=='-')
                {
                    co++;
                for(int jo=i;jo<=(i+ko-1) && (i+ko-1)<l ;jo++)
                    {
                        if(s1[jo]=='+')
                s1[jo]='-';
                        else
                s1[jo]='+';
                    }
                }
            }
            for(int i=0;i<l;i++)
            {
                if(s1[i]=='-')
                {
                    go=1;
                    break;
                }
            }
            if(go!=1)
                {cout<<"Case #";
                cout<<man-test<<": "<<co<<endl;}
            else
                {cout<<"Case #";
                cout<<man-test<<": ";
                cout<<"IMPOSSIBLE"<<endl;}
        }
    }
}
