#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define rep(i,a) for(int i=0;i<(int)a;i++)
#define repp(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define fill(a,x) memset(a,x,sizeof(a))
#define foreach( gg, itit) for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const int mod  = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

#define ld long double
//#define double long double
const ld EPS=1e-12;

int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int ca=0;
	while(t--){
		string s;
		cin>>s;
		int n=s.size();
		int k;
		cin>>k;
		//cout<<k<<endl;
		int net=0;
		for(int i=n-1;i>=k-1;i--){
			//cout<<i<<" "<<s[i]<<endl;
			if(s[i]=='-'){
				rep(j,k){
					if(s[i-j] == '-'){
						s[i-j]='+';
					}else{
						s[i-j]='-';
					}
				}
				net++;
			}
		}
		int flag=0;
		rep(i,n){
			if(s[i] == '-'){
				flag=1;
				break;
			}
		}
		ca++;
		cout<<"Case #"<<ca<<": ";
		if(flag == 1){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<net<<endl;
		}
	}
	return 0;
}

