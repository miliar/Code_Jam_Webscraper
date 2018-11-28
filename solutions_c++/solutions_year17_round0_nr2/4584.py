#include<bits/stdc++.h>
//#include<windows.h>

#define nl              cout<<"\n"
#define sz(x)           (int)((x).size())
#define len(x)          (x).length()
#define all(a)          (a).begin(),(a).end()
#define rep(i,n)        for( int i=0;i<(int)(n);i++)
#define brep(i,n)       for( int i=(n);i>=0;i-- )
#define repp(i,a,b)     for( int i = (a); i < (b); i++ )
#define ll      long long int
#define pb      push_back
#define mp      make_pair
#define F       first
#define S       second
#define vi      vector<int>
#define vll     vector<ll>
#define pii     pair<int,int>
#define vpii    vector<pair<int,int> >
#define bits    __builtin_popcountll
#define mod     1000000007
#define test int tes; cin >> tes; while( tes-- > 0 )
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
ll a,b,x,y,n,m,t,p,q;



int main()
{
   freopen("B-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);
    fast
    x=1;
	string ans,k;
	test
	{
	ans="",k="";
	cin>>k;
	int i,j;
	for(i=0;i<len(k)-1;i++)
	{
		if(k[i] > k[i+1])
			break;
	}
	if(i==len(k)-1)
		ans = k;
	else
	{
	//	cout<<"i="<<i,nl;
		for(j=i;j>=0;j--)
		{
			if(k[j] !=k[j-1] )
				break;
		}
	//	cout<<"j="<<j,nl;
		ans = k.substr(0,j);
	//	cout<<ans,nl;
		ans.pb(k[j]-1);
		repp(ii,j+1,len(k))
			ans.pb('9');
		string temp = "";
		for(i=0;i<len(ans)&&ans[i]=='0';i++);
		for(;i<len(ans);i++)
			temp += ans[i];
		ans = temp;
	}
	
	cout<<"Case #"<<x++<<": "<<ans<<"\n";
	}

//    ShellExecute(NULL,"open","op.txt",NULL,NULL,SW_SHOWNORMAL);
}
