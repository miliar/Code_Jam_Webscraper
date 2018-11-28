
#include <bits/stdc++.h>
using namespace std;

#define fill(a,val) memset(a, (val), sizeof a)
#define pb push_back
#define lli long long int
#define scantype int
#define endl "\n"
#define unique(x) x.erase(unique(x.begin(),x.end()), x.end())

lli MOD  = 1000000007;
lli inf = 1e15;

void scan(scantype &x);
lli powermod(lli _a,lli _b,lli _m){lli _r=1;while(_b){if(_b%2==1)_r=(_r*_a)%_m;_b/=2;_a=(_a*_a)%_m;}return _r;}
lli string_to_number(string s){lli x=0; stringstream convert(s); convert>>x; return x;}
lli add(lli a,lli b){lli x = (a+b)%MOD; return x; }
lli mul(lli a,lli b){lli x = (a*b)%MOD; return x; }
lli sub(lli a,lli b){lli x = (a-b+MOD)%MOD; return x; }
lli divi(lli a,lli b){lli x = a;lli y = powermod(b,MOD-2,MOD);lli res = (x*y)%MOD;return res;}

#define N 100003

map<int,char> color;

void solve(int testcase)
{
	int n,a[6];

	cin>>n;

	for(int i=0;i<6;i++) cin>>a[i];

	vector< pair<int,int> > tmp;

	tmp.pb({a[0],0});
	tmp.pb({a[2],2});
	tmp.pb({a[4],4});

	sort(tmp.begin(),tmp.end());

	if(tmp[0].first+tmp[1].first<tmp[2].first)
	{
		printf("Case #%d: IMPOSSIBLE\n",testcase);
		return;
	}

	vector<char> vp;

	int i;

	for(i=0;i<tmp[2].first;i++)
		vp.pb(color[tmp[2].second]);

	int firstTime = 1;

    for(i=0;i<vp.size() && tmp[0].first;i=(i+1)%vp.size())
    {
    	char currColor = color[tmp[0].second];

    	int pos = i+1;

    	if(firstTime)
    	{
    		firstTime = 0;
    		pos = i;
    	}
    
    	if(vp[i]!=currColor)
    		vp.insert(vp.begin()+pos,currColor),tmp[0].first--;

    	
    }

    for(;i<vp.size() && tmp[1].first;i = (i+1)%vp.size())
    {
    	char currColor = color[tmp[1].second];

    	int pos = i+1;
    	
    	if(firstTime)
    	{
    		firstTime = 0;
    		pos = i;
    	}

    	if(vp[i]==color[tmp[2].second])
    		vp.insert(vp.begin()+pos,currColor),tmp[1].first--;

    }
    
    string st;
    for(auto it : vp) st+=it;

    int flag = 0;
    for(int i=0;i<st.length()-1;i++)
    {
    	if(st[i]==st[i+1])
    	{
    		flag = 1;
    	}
    }
    if(st[0]==st[st.length()-1] | flag)
    {
    	cerr<<"fucked at: "<<testcase<<endl<<endl;
    }

    cout<<"Case #"<<testcase<<": "<<st<<endl;

}
void pre()
{
	string st = "ROYGBV";
	for(int i=0;i<st.length();i++)
		color[i] = st[i];
}
int main(void)
{
  pre();
  int t;
  cin>>t;

  for(int i=1;i<=t;i++)
  	solve(i);
  return 0;
}


void scan(scantype &x)
{
    register int c = getchar(); //for negative/positive
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = getchar());
    if(c=='-') {neg=1;c=getchar();}
    for(;c>47 && c<58;c = getchar()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

