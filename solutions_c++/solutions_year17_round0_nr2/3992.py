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
#define Frst	first
#define Sec		second
#define Dup erase(unique(V.begin(),V.end()),V.end())

#define TC int test; cin>>test; test++; while(--test)

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
    #ifndef ONLINE_JUDGE
    freopen("B-large.txt","r",stdin);
    freopen("Tidy_numbers__out_large.txt","w",stdout);
    #endif // ONLINE_JUDGE*/

    lli T,t=1;
    cin>>T;
    while(T--)
    {
        lli N;
        cin>>N;
        cout<<"Case #"<<t++<<": ";

        lli cnt=0,i=1;
        stack<lli>S;

        lli Max=0;

        while(i<=9 && i<=N)
        {
        	S.push(i);

        	Max=max(Max,i);
        	i++;
        }

        while(!S.empty())
        {
        	lli Top=S.top();
        	S.pop();

        	for(lli j=Top%10;j<=9;++j)
        	{
        		lli x=Top*10+j;

        		if(x<=N)
        		{
        			S.push(x);

        		    Max=max(Max,x);

        		}
        	}
        }

        cout<<Max;
        cout<<'\n';
    }




return 0;
}
