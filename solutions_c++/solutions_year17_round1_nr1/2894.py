
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
    freopen("A-small-attempt1.in","r",stdin);
    freopen("double_squares_out.txt","w",stdout);
    #endif // ONLINE_JUDGE*/

    lli T,t=1;
    cin>>T;

    while(T--)
    {
        lli Count[26]={0};

        lli R,C,i,j,k;
        cin>>R>>C;

        string s;
        char a[R+2][C+2];

        rep(i,0,R+2)
        {
            rep(j,0,C+2)
            {
                a[i][j]='?';
            }
        }

        rep(i,1,R+1)
        {
            rep(j,1,C+1)
            {
                cin>>a[i][j];

                if(a[i][j]!='?')
                {
                    Count[i]++;
                }
            }
        }

        cout<<"Case #"<<t++<<":";
        nl;

        rep(i,1,R+1)
        {
            rep(j,1,C+1)
            {
                if(a[i][j]=='?')
                {
                    I flag=0;
                    repr(k,j-1,-1)
                    {
                        if(a[i][k]!='?')
                        {
                            flag=1;
                            a[i][j]=a[i][k];

                            break;
                        }
                    }

                    if(flag)
                    {
                        continue;
                    }

                    rep(k,j+1,C+2)
                    {
                        if(a[i][k]!='?')
                        {
                            a[i][j]=a[i][k];
                            break;
                        }
                    }
                }
            }
        }

        rep(i,1,R+1)
        {
            if(Count[i])
            {
                repr(j,i-1,0)
                {
                    if(!Count[j])
                    {
                        rep(k,1,C+1)
                        {
                            a[j][k]=a[i][k];
                        }
                        Count[j]=1;
                    }
                    else
                    {
                        break;
                    }
                }

                rep(j,i+1,R+1)
                {
                    if(!Count[j])
                    {
                        rep(k,1,C+1)
                        {
                            a[j][k]=a[i][k];
                        }
                        Count[j]=1;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }

        rep(i,1,R+1)
        {
            rep(j,1,C+1)
            {
                cout<<a[i][j];
            }
            nl;
        }
    }



 return 0;
}
