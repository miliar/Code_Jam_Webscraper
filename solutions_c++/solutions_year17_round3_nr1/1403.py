    #include<bits/stdc++.h>
    #include<string>
    using namespace std;
    typedef long long ll;
    typedef long double ld;
    typedef pair<ll,ll > pii;
    typedef pair<long,pii > piii;
    typedef vector<long long >   VI;
    #define sc1(x) scanf("%lld",&x);
    #define sc2(x,y) scanf("%lld%lld",&x,&y);
    #define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);
    #define pb push_back
    #define mp make_pair
    #define ini(x,val) memset(x,val,sizeof(x));
    #define fs first
    #define sc second
    #define MOD 1000000007
    #define inf 99999999999999ll	//long long inf
    #define PI 3.1415926535897932384626

    #define gcd __gcd
    #define tr(contaner, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
    #define PrintCont(cont) {cout<<("\n----------------\n");\
    for(typeof(cont.begin()) it = cont.begin();it!=cont.end();++it) cout<<*it<<" ";cout<<("\n----------------\n");}
    #define all(v) v.begin(),v.end()
    #define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

    #define debug(x) cout<<#x<<" :: "<<x<<"\n";
    #define debug2(x,y) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
    #define debug3(x,y,z) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";

    int main()
    {
        
        //freopen("input.txt","r",stdin);
        //freopen("out.txt","w",stdout);
        ll t,cas=0;
        cin>>t;
        while(t--)
        {
            cas++;
            vector<pii> vect;
            ll n,k,r[1010],h[1010];
            double ans=-1000000.00;
            cin>>n>>k;
            for(int i=0;i<n;i++)
            {
                cin>>r[i]>>h[i];
                vect.pb(mp(r[i]*h[i],i));
            }
            sort(vect.begin(),vect.end());
            for(int i=0;i<n;i++)
            {
                ll bot=r[i];
                double sum=PI*r[i]*r[i]+2*PI*r[i]*h[i];
                ll cnt=1;
                for(int j=n-1;j>=0;j--)
                {
                    ll idx=vect[j].sc;
                    if(r[idx]<=bot&&cnt<k&&idx!=i)
                    {
                        sum+=(2*PI*r[idx]*h[idx]);
                        cnt++;
                    }
                }
                if(cnt==k)
                {
                    ans=max(ans,sum);
                }
            }
             cout<<"Case #"<<cas<<": ";
             printf("%.8lf\n",ans);
        }
        return 0;
    }