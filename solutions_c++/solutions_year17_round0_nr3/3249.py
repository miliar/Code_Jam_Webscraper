#include<bits/stdc++.h>

using namespace std;

#define fRead(x)  freopen(x,"r",stdin)
#define fWrite(x) freopen (x,"w",stdout)

#define LL long long
#define ULL unsigned long long
#define ff first
#define ss second
#define pb push_back
#define INF 2e16
#define PI acos(-1.0)
#define mk make_pair
#define pii pair<int,int>
#define pll pair<LL,LL>


#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(a,min(b,min(c,d)))
#define max4(a,b,c,d) max(a,max(b,max(c,d)))
#define SQR(a) ((a)*(a))
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define ROF(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,b) for(int i=0;i<b;i++)
#define MEM(a,x) memset(a,x,sizeof(a))
#define ABS(x) ((x)<0?-(x):(x))

#define scanI(a) scanf("%d",&a)
#define scanI2(a,b) scanI(a) , scanI(b)
#define scanI3(a,b,c) scanI(a), scanI(b), scanI(c)
#define scanI4(a,b,c,d) scanI(a), scanI(b), scanI(c), scanI(d)

#define scanL(a) scanf("%I64d",&a)
#define scanL2(a,b) scanL(a) , scanL(b)
#define scanL3(a,b,c) scanL(a), scanL(b), scanL(c)
#define scanL4(a,b,c,d) scanL(a), scanL(b), scanL(c), scanL(d)

#define SORT(v) sort(v.begin(),v.end())
#define REV(v) reverse(v.begin(),v.end())


#define FastRead ios_base::sync_with_stdio(0);cin.tie(nullptr);


int main()
{
    freopen("Clarge.in","r",stdin);
    freopen("out.txt","w",stdout);
     LL t,cases=0;
     cin >> t;
     while(t--){
        LL n,k;
        cin >> n >> k;

        priority_queue<LL>Q;
        map<LL,LL>mp;

        Q.push(n);
        mp[n] = 1;

        LL timer = k;
        while(timer>0)
        {
            LL value = Q.top();
            Q.pop();

            LL L = (value-1)/2;
            LL R = value - L - 1;
            if(L>0)
            {
                if(mp[L]==0)Q.push(L);
                mp[L]+=mp[value];
            }
            if(R>0)
            {
                if(mp[R]==0)Q.push(R);
                mp[R]+=mp[value];
            }
            timer -= mp[value];

            mp[value]=0;
            if(timer<=0){
                cout << "Case #" << ++cases <<": ";
                cout << value/2 << " " << (value-1)/2 << "\n";
                break;
            }
        }
     }

}
