#include <bits/stdc++.h>
using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0);cout.tie(0); } } _;
#define READ(FILE) freopen(FILE,"r",stdin)
#define WRITE(FILE) freopen(FILE,"w",stdout)
#define ict int t;cin>>t;while(t--)
#define lct long long int t;cin>>t;while(t--)
#define in(a) int a; cin>>a;
#define llin(a) ll a; cin>>a;
#define srep(i,a,b) for(ll i=a;i<b;i++)
#define rep(i,n) for(ll i=0;i<n;i++)
#define pb push_back
template <typename T> std::string to_str(T value) {std::ostringstream os;os << value ;return os.str();}
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef set<int> si;
typedef set<ll> sl;
typedef map<string, ll> mapsl;
typedef map<string, int> mapsi;
typedef map<int,int> mapii;
typedef map<ll, ll> mapll;

bool increasing(string str)
{
    for(int i=1;i<str.length();i++)
    {
        if(str[i]<str[i-1])
            return false;
    }
    return true;
}

string maxIncString(string str)
{
    for(int i=1;i<str.length();i++)
    {
        if(str[i]<str[i-1])
        {
            int j=i-1;
            while(j>=0)
            {
                if(str[j]>='0')
                {
                    str[j]--;
                    for(int k=j+1;k<str.length();k++)
                        str[k]='9';
                    return maxIncString(str);
                }
            }
        }
    }
    return str;
}

string removeLeadZero(string str)
{ return str.erase(0, min(str.find_first_not_of('0'), str.size()-1)); }

int main()
{
    freopen("inputFiles/B-large.in","r",stdin);
    freopen("inputFiles/ans.txt","w",stdout);
    llin(T);
    for(ll t=1;t<=T;t++)
    {
        string str;cin>>str;
        cout<<"Case #"<<t<<": "<<removeLeadZero(maxIncString(str))<<endl;
    }

}
