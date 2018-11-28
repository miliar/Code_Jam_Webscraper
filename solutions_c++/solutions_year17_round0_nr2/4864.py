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
#define in int n;sc(n);
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
    int jam=1;
    tl
    {
        ll num;
        cin>>num;
        vector<int> arra(19);
        int ja=0;
        for(int p=0;p<=18;p++)
            arra[p]='$';
        while(num!=0)
        {
            arra[ja]=num%10;
            ja++;
            num=num/10;

        }
        for(int i=1;i<ja;i++)
        {
            if(arra[i]>arra[i-1])
            {
                arra[i]=arra[i]-1;
                for(int k=0;k<=i-1;k++)
                   arra[k]=9;
                }
        }
        int gun=0;
        for(int i=ja-1;i>=0;i--)
        {
            if(arra[i]==0)
            gun++;
            else
                break;
        }
        cout<<"Case #";
        cout<<jam<<": ";
        jam++;
        for(int i=ja-1-gun;i>=0;i--)
        {
          cout<<arra[i];
        }
        cout<<endl;
    }
}
