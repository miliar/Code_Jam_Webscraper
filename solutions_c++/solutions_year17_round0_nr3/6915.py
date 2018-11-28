#include<bits/stdc++.h>
using namespace std;

// my choco pie
#define pb push_back
#define mp make_pair
#define pob pop_back
#define VI vector<int>
#define VL vector<long long int >
#define VP vector<pair < int,int > >

// my fastest car series
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define scanllu(x) scanf("%llu",&x)
#define printll(x) printf("%lld\n",x)
#define printllu(x) printf("%llu\n",x)
#define ms(x) memset(x,0,sizeof(x))

// data pies
#define ll long long int
#define li long int
#define ff float
#define db double

// loopi loops
#define rep(i,a,b) for(i=a;i<b;i++)
#define repr(i,a,b) for(i=a;i>=b;i--)

// debugger
#define print_v(x) for(int i=0;i<x.size();i++) cout << x[i] << " "

#define IOS ios_base::sync_with_stdio(false); cin.tie(NULL)
#define MOD 1000000007

int main(){
	fstream fin("C-small-2-attempt0.in");
	fstream fout("C-small-2-attempt0.out");
	if(!fin.is_open()||!fout.is_open()){
		cout<<"FUCK";
		return 0;
	}
	//fout<<fixed;
	//fout<<setprecision(9);
	//fout<<"Case #"<<ctr<<":\n";
	int tc=1,t;
	fin>>t;
	while(tc<=t){
		ll n,k,mx,mn;
		fin>>n>>k;
		VL hp;
		hp.pb(n);
		while(k--){
			pop_heap(hp.begin(),hp.end());
			ll ele = hp[hp.size()-1];
			hp.pop_back();
			if(ele&1){
				ll hlf = ele>>1;
				mx = hlf;mn=hlf;
			}else{
				ll hlf = ele>>1;
				mx = hlf;
				mn = hlf-1;
			}
			hp.pb(mx);
			push_heap(hp.begin(),hp.end());
			hp.pb(mn);
			push_heap(hp.begin(),hp.end());
		}
		
		fout<<"Case #"<<tc<<": "<<mx<<" "<<mn<<endl;
		tc++;
	}
	return 0;
}
