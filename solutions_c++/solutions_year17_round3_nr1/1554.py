/*I MAY NOT GET THE SUCCESS IMMEDIATELY BUT I WILL GET IT FOR SURE*/
#include<bits/stdc++.h>
#define opt std::ios_base::sync_with_stdio(false)
#define I int
#define li		int32_t
#define lli		long long
#define ulli unsigned long long

#define pn			printf("\n")
#define nl			cout<<'\n'
#define sf(N)       scanf("%lld",&N)
#define pf(N)       printf("%lld",N)
#define sl          cout<<' '
#define ps          printf(" ")

#define rep(i,a,b)	for(i=a;i<b;i++)
#define repr(i,a,b)	for(i=a;i>b;i--)
#define elif		else if
#define mset(a,b)	memset(a,b,sizeof(a))

#define pb		push_back
#define pob		pop_back
#define itr		iterator
#define sz()	size()
#define szof    sizeof
#define lb		lower_bound
#define ub		upper_bound
#define mp		make_pair
#define vlli    vector<lli>
#define plli	pair<lli,lli>
#define vplli	vector<plli >
#define F   	first
#define S		second
#define Dup erase(unique(V.begin(),V.end()),V.end())

#define Inf     1000000000000000
#define mod		1000000007
using namespace std;

bool comp(const pair<lli,lli> &a,const pair<lli,lli> &b)
{
    if(a.F*a.S==b.F*b.S)
    {
        return (a.F>b.F);
    }

    return (a.F*a.S>b.F*b.S);
}

lli Power(lli a,lli b)
{
    lli result=1;

    while(b)
    {
        if(b%2)
        {
            result=(result*a)%mod;
        }

        b=b>>1;
        a=(a*a)%mod;
    }

 return result;
}

int main()
{
    opt;

    #ifndef ONLINE_JUDGE
    freopen("A1.in","r",stdin);
    freopen("double_squares_out.txt","w",stdout);
    #endif // ONLINE_JUDGE*/

    lli T,t=1;
    cin>>T;

    while(T--)
    {
        lli N,i,K,j;
        cin>>N>>K;

        vplli V(N);
        rep(i,0,N)
        {
            cin>>V[i].F>>V[i].S;
        }

        cout<<"Case #"<<t++<<": ";

        sort(V.begin(),V.end(),comp);

        /*rep(i,0,V.sz())
        {
            cout<<V[i].F<<' '<<V[i].S;
            nl;
        }*/

        double Maximum=0;
        rep(i,0,N)
        {
            lli cnt=0;
            rep(j,0,N)
            {
                if(V[i].F>=V[j].F)
                {
                    cnt++;
                }
            }

            if(cnt>=K)
            {
                double Maximum1=0,pi=acos(-1);
                lli cnt=0;

                rep(j,0,N)
                {
                    if(V[i].F>=V[j].F)
                    {
                        if(cnt==K-1)
                        {
                            if(j<i)
                            {
                                continue;
                            }
                            else
                            {
                                Maximum1+=2*pi*V[j].F*V[j].S;
                                cnt++;
                            }
                        }

                        if(cnt<K)
                        {
                            Maximum1+=2*pi*V[j].F*V[j].S;
                            cnt++;
                        }
                        else
                        {
                            break;
                        }
                    }
                }

                if(j>=i)
                {
                    Maximum=max(Maximum1+pi*V[i].F*V[i].F,Maximum);
                }
            }
        }

        cout<<setprecision(10)<<fixed<<Maximum;
        nl;
    }




 return 0;
}
