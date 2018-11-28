/*	Success may not come to me immediately,
 *	but it will come definitely....
 */
#include<bits/stdc++.h>
#include<tr1/unordered_set>
#include<tr1/unordered_map>
//=====================================================================
using namespace std;
using std::tr1::unordered_set;
using std::tr1::unordered_map;
//=====================================================================
#define opt	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
//=====================================================================
#define li	int64_t
#define ld	double_t
#define ulli	uint64_t
//=====================================================================
#define rep(i,a,b)	for(i=a;i<b;i++)
#define repr(i,a,b)	for(i=a;i>b;i--)
#define repi(i,v)	for(i=v.begin();i!=v.end();i++)
#define elif		else if
#define mset(a,b)	memset(a,b,sizeof(a))
#define nl		cout<<'\n'
//=====================================================================
typedef vector<li>       vli;
typedef vector<string>	 vstr;
typedef pair<li,li>      pli;
typedef pair<li,pli >    ppli;
typedef pair<li,ppli >   pppli;
typedef vector<pli >     vpl;
typedef vector<ppli >    vppli;
typedef vector<pppli >   vpppli;
//=====================================================================
#define pb	push_back
#define pob	pop_back
#define pf	push_front
#define pof	pop_front
#define all(v)	v.begin(),v.end()
#define itr	iterator
#define sz	size()
#define lb	lower_bound
#define ub	upper_bound
#define bs	binary_search
#define mp	make_pair
#define F	first
#define S	second
//=====================================================================
#define mod	1000000007
#define inf	1000000000000000005
#define MX1	100005
#define MX2	1000005
#define pi	acos(-1)
//=====================================================================
li power(li a,li b){li ans=1;while(b){if(b&1)
{ans=(ans*a)%mod;}a=(a*a)%mod;b>>=1;}return ans;}
//=====================================================================
li mmi(li n){return power(n,mod-2);}
//=====================================================================
/*------------------------MAIN CODE BEGINS NOW!------------------------*/

li cases=0;

void solve(){
    li n,i,j;cin>>n;
    string s;
    ostringstream temp;
    temp<<n;
    s=temp.str();
    rep(j,0,s.length()){
        rep(i,0,s.length()-1){
            if(s[i]>s[i+1]){
                s[i]=s[i]-1;
                break;
            }
        }
        rep(i,i+1,s.length()){
            s[i]='9';
        }
    }
    i=0;
    while(s[i]=='0'){
        i++;
    }
    cout<<"Case #"<<++cases<<": ";
    string a="";
    rep(i,i,s.length()){
        a+=s[i];
    }
    cout<<a;nl;
}

int main(){
    opt
    li t;cin>>t;while(t--){
        solve();
    }
    return 0;
}
