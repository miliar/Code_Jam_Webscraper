/*Till Death do us Part......... */

#include <bits/stdc++.h>
using namespace std;
#define ff first
#define re return
#define ss second
#define pb push_back
#define mpk make_pair
#define couts(a) cout<<a<<"\n"
#define fr(i,a,b) for(int i=a;i<b;++i)
#define ioS ios_base::sync_with_stdio(0)
#define coutd(a,b) cout<<a<<" "<<b<<"\n"

//============================DEBUG==========================================
#define trace(a) cout<<#a<<": "<<a<<endl
#define trace2(a,b) cout<<#a<<": "<<a<<" | " <<#b<<": "<<b<<endl;
#define trace3(a,b,c) cout<<#a<<": "<<a<<" | " <<#b<<": "<<b<<" | "<<#c<<": "<<c<<endl;
//============================================================================

typedef long long int ll;
typedef long double ld;
typedef pair<ll,ll>pi;
typedef long long int ll;
typedef vector<int> vi;

const ll MAXN=1e6+10;
const int MOD=1e9+7;

string ans(string s)
{
	int bo=0;
	fr(i,1,s.length())
	{
		if(s[i]<s[i-1])bo=1;
	}
	if(bo==0)re s;
	char c=s[0];
	int pos=0;
	for(int i=1;i<s.length();i++)
	{
		if(s[i]<=s[i-1])break;
		pos=i;
	}
	int i=0;
	string temp="";
	while(i!=pos){temp+=s[i];i++;}
	temp+=char(s[pos]-1);i++;
	while(i<s.length()){temp+="9";i++;}
	string f="";
	i=0;
	while(temp[i]=='0')i++;
	while(i<temp.length()){f+=temp[i];i++;}
	re f;
}

int main()
{

	//freopen("test.txt","r",stdin);
	freopen("bsmall.in","r",stdin);
	freopen("Bout.txt","w",stdout);
	ioS;
	int t;
	cin>>t;

	fr(x,1,t+1)
	{
		string s;
		cin>>s;
		string a=ans(s);

		cout<<"Case #"<<x<<": ";
		couts(a);

	}

}



