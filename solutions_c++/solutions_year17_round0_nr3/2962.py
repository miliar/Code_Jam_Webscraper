#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define pll pair<LL, LL>
#define pii pair<int,int>

#define mp make_pair
#define pb push_back
#define fs first
#define sc second

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define EPS 1e-6
#define MOD (1000000007)
#define PI  2*acos(0);

#define fore(iter,v) for(iter=v.begin(); iter!=v.end(); iter++)
#define forup(i,a,n) for(i=a; i<n; i++)
#define rep(i,n) for(i=0; i<n; i++)
#define SET(a, v) memset(a, v, sizeof a)
#define all(a) a.begin(),a.end()
#define ALLOC0(N)   (int*)calloc(N, sizeof(int));

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)


#define ps(x) printf("%s",x)
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld", x)
#define pn printf("\n")
#define spc printf(" ")
#define gc getchar


map<ll,ll>::iterator it;
map<ll,ll> mymap;

bool ins(ll num,ll q)
{
    if(num==0)
        return false;
    it = mymap.find(num);
    if(it!=mymap.end())
    {
        it->second+=q;
        return false;
    }
    else
    {
        mymap.insert(make_pair(num,q));
        return true;
    }

}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,bk;
    cin>>t;
    for(bk=1;bk<=t;bk++)
    {
        mymap.clear();
        cout<<"Case #"<<bk<<": ";
        ll n,k,i,c,num,num1,num2;
        priority_queue<ll> mypq;
        cin>>n>>k;
        mymap.insert(make_pair(n,1));
        mypq.push(n);
        i=0;
        while(1)
        {
            c=mypq.top();
            mypq.pop();
            it = mymap.find(c);
            num=it->second;
            mymap.erase(it);
            if(c%2==0)
            {
                num1=c/2-1;
                num2=c/2;
                if(i+num<k)
                {
                    if(ins(num1,num))
                        mypq.push(num1);
                    if(ins(num2,num))
                        mypq.push(num2);
                }
                else
                {
                    cout<<max(num1,num2)<<" "<<min(num1,num2)<<endl;
                    break;
                }


            }
            else
            {
                num1=(c-1)/2;
                if(i+num<k)
                {
                    if(ins(num1,2*num))
                        mypq.push(num1);
                }
                else
                {
                    cout<<num1<<" "<<num1<<endl;
                    break;
                }
            }
            i+=num;
        }

    }
    return 0;
}
