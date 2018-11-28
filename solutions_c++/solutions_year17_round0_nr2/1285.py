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
    #define inf 999999999999999ll	//long long inf
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


    bool check(string str)
    {
        bool ans=true;
        int len=str.length();
        for(int i=1;i<len;i++)
        {
            if(str[i]<str[i-1])
            {
                ans=false;
                break;
            }
        }
        return ans;
    }

    int main()
    {
        freopen("input.txt","r",stdin);
        freopen("out.txt","w",stdout);
        ll t,cas=0;
        cin>>t;
        while(t--)
        {
            string str,str1;
            cas++;
            cin>>str;
            str1=str;
            ll n=str.length();
            if(check(str1)==true)
            {

            }
            else
            {
                for(int i=n-1;i>=0;i--)
                {
                    if(str[i]!='0')
                    {
                        str1=str;
                        str1[i]=str1[i]-1;
                        for(int j=i+1;j<n;j++)
                        {
                            str1[j]='9';
                        }
                        if(check(str1)==true)
                        {
                            break;
                        }
                    }
                }
            }
            string str2="";
            int k=0;
            while(str1[k]=='0')
            {
                k++;
            }
            for(int i=k;i<n;i++)
            {
                str2.append(1,str1[i]);
            }
            cout<<"Case #"<<cas<<": ";
            cout<<str2<<endl;
        }

        
        return 0;
    }