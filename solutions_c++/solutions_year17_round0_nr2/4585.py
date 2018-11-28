#include<bits/stdc++.h> //_Shaffi
using namespace std;
#define sc scanint
#define sl scanlong
#define gc getchar
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define in(a,arr) sc(a); arr.push_back(a);
#define mi 100000007
#define DO int t; scanf("%d",&t); while(t--)
#define st(arr); sort(arr.begin(),arr.end());
#define er(arr); arr.erase(unique(arr.begin(),arr.end()),arr.end());
#define INF INT_MAX
#define mx(arr) *max_element(arr.begin(),arr.end())
#define mn(arr) *max_element(arr.begin(),arr.end())
#define getst(s) getline(cin>>ws,s)
#define sci(a,b) sc(a),sc(b);
#define scl(a,b) sl(a),sl(b);
#define MAX 664579
typedef long long ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > pi;
void scanint(int &x);
void scanlong(ll &x);
void scanint(int &x)
{
        int flag=0;
        register int c = gc();
        if(c == '-') flag=1;
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
        if(flag == 1)x=-x;
}
void scanlong(ll &x)
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
    int b=1;
    DO
    {
        ll n; sl(n);
        vector<int>a(19);
        int j=0,k,i;
        for(i=0;i<=18;i++)
            a[i]='$';
        while(n!=0)
        {
            a[j]=n%10;
            n=n/10;
            j++;
        }
        for(i=1;i<j;i++)
        {
            if(a[i]>a[i-1])
            {
                a[i]=a[i]-1;
                for(k=0;k<=i-1;k++)
                   a[k]=9;
                }
        }
        int g=0;
        for(i=j-1;i>=0;i--)
        {
            if(a[i]==0)
            g++;
            else
                break;
        }
        cout<<"Case #"<<b<<": ";
        b++;
        for(i=j-1-g;i>=0;i--)
        {
          cout<<a[i];
        }
        cout<<"\n";
    }
}
