//template by murugappan....Copied from chamow :p

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define priq(i,comp) priority_queue( i, vector< i >,comp)

template<class t>
t lcm(t a,t b)
{
    return ((a*b)/__gcd(a,b));
}

#define fastread ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

#define maxn 10000000
// root(n) prime check
bool isprime(ll num)
{
    if(num==1)
    return false;
    ll limit=sqrt(num);
    if(num==2)
    return true;
    if(num%2==0)
    return false;
    for(ll i=3;i<=limit;i+=2)
    {
        if(num%i==0)
        {
            return false;
        }
    }
    return true;
}
//end of template
ll arr[6];
ll red,orange,yellow,green,blue,violet;
ll redc,yellowc,bluec;
int c;
int main()
{
    assert(freopen("input.txt","r",stdin));
  assert(freopen("output.txt","w",stdout));
    int t;
    cin>>t;
    char ans[]={'R','O','Y','G','B','V'};
    while(t--)
    {
        c++;
        cout<<"Case #"<<c<<": ";
        int n;
        cin>>n;
        ll lim=n/2;
        cin>>red>>orange>>yellow>>green>>blue>>violet;
        arr[0]=red;
        arr[1]=orange;
        arr[2]=yellow;
        arr[3]=green;
        arr[4]=blue;
        arr[5]=violet;
        redc=red+orange+violet;
        yellowc=yellow+green+orange;
        bluec=blue+green+violet;
        if(redc>lim || yellowc>lim || bluec>lim)
        {
            cout<<"IMPOSSIBLE";
        }
        else
        {
            for(ll i=0;i<6;i++)
            {
                if(arr[i]==0)
                    continue;
                ll cur=i;
                while(cur!=-1)
                {
                    cout<<ans[cur];
                    arr[cur]--;
                    if(cur==0)
                    {
                        if(arr[3]!=0)
                        {
                            cur=3;
                        }
                        else if(arr[2]==0 && arr[4]==0)
                        {
                            cur=-1;
                        }
                        else if(arr[2]>=arr[4])
                            cur=2;
                        else
                            cur=4;
                    }
                    else if(cur==1)
                    {
                        if(arr[4]!=0)
                            cur=4;
                        else
                            cur=-1;
                    }
                    else if(cur==3)
                    {
                        if(arr[0]!=0)
                            cur=0;
                        else
                            cur=-1;
                    }
                    else if(cur==5)
                    {
                        if(arr[2]!=0)
                            cur=2;
                        else
                            cur=-1;
                    }
                    else if(cur==2)
                    {
                        if(arr[5]!=0)
                            cur=5;
                        else if(arr[0]==0 && arr[4]==0)
                            cur=-1;
                        else if(arr[0]>=arr[4])
                            cur=0;
                        else
                            cur=4;
                    }
                    else if(cur==4)
                    {
                        if(arr[1]!=0)
                            cur=1;
                        else if(arr[0]==0 && arr[2]==0)
                            cur=-1;
                        else if(arr[0]>=arr[2])
                            cur=0;
                        else
                            cur=2;
                    }
                }

            }
        }
        cout<<"\n";
    }
    return 0;
}

