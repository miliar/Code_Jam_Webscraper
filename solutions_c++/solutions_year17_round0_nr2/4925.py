#include<bits/stdc++.h>
using namespace std;
#define gc getchar
#define mp make_pair
#define f first
#define mi 1000000007
#define itr int t;cin>>t;while(t--)
#define sl scanlong
typedef vector<int> vi;
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
int main()
{
    int shvu=1;
    itr
    {
        long long int mas; cin>>mas;
        vector<int> vec(19);
        for(int z=0;z<=18;z++)
            vec[z]='$';
        int ju=0;
        while(mas!=0)
        {
            vec[ju]=mas%10;
            mas=mas/10;
            ju++;
        }
        for(int i=1;i<ju;i++)
        {
            if(vec[i]>vec[i-1])
            {
                vec[i]=vec[i]-1;
                for(int ku=0;ku<=i-1;ku++)
                   vec[ku]=9;
                }
        }
        int germ=0;
        for(int i=ju-1;i>=0;i--)
        {
            if(vec[i]==0)
            germ=germ+1;
            else
                break;
        }
        cout<<"Case #";
        cout<<shvu<<": ";
        shvu++;
        for(int iq=ju-1-germ;iq>=0;iq--)
        {
          cout<<vec[iq];
        }
        cout<<endl;
    }
}
