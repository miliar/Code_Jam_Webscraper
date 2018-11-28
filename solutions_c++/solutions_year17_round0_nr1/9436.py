#include<bits/stdc++.h>

#define pi acos(-1)
#define eps 1e-9
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define mem(a,b) memset(a,b,sizeof(a))
#define clock 1.0*clock()/CLOCKS_PER_SEC
#define filein freopen("in.txt","r",stdin)
#define fileout freopen("out.txt","w",stdout)
#define fast std::ios::sync_with_stdio(false);cin.tie(NULL)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const int dr[]={0,-1,0,1,-1,-1,1,1};
const int dc[]={1,0,-1,0,1,-1,-1,1};
const int maxx = 0;

int k;
string s;

void process(int pos){
	for(int i=pos,j=0;j<k;i++,j++){
		if(s[i]=='+') s[i]='-';
		else s[i]='+';
	}
	//cout<<s<<endl;
}

int main ()
{
//	filein;
//	fileout;
	int a;
	cin>>a;
	for(int i=0;i<a;i++){
		cout<<"Case #"<<i+1<<": ";
		cin>>s>>k;
		int m=0;
		for(int j=0;j<s.size()-k+1;j++){
			if(s[j]=='-'){
				process(j);
				m++;
			}
		}
		bool ok = true;
		for(int j=0;j<s.size();j++){
			if(s[j]=='-') ok = false;
		}
		if(!ok) cout<<"IMPOSSIBLE"<<endl;
		else cout<<m<<endl;
	}
    return 0;
}

