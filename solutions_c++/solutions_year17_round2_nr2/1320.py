#include<bits/stdc++.h>

#define REP(i,s,n) for(int (i)=s; (i)<(int)(n);(i)++)
#define RIT(it,c) for(__typeof(c.begin()) it = c.begin();it!=c.end();it++)
#define ALL(x) x.begin(), x.end()
#define SZ(x) (int)(x).size()
#define MSET(m,v) memset(m,v,sizeof(m))


using namespace std;


typedef long long LL;
typedef long double LD;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<LL> vL;
typedef vector<bool> vb;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::ios_base::sync_with_stdio(false),cin.tie(0),cout.tie(0);
    freopen("B-small-attempt1.in","r",stdin);
    freopen("output_small","w",stdout);
    int T;
    cin>>T;
    cerr<<T<<endl;
    for(int t=1;t<=T;++t){
        cout<<"Case #"<<t<<": ";
        cerr<<"Case #"<<t<<": ";     
		int N,R,O,Y,G,B,V;
		cin>>N>>R>>O>>Y>>G>>B>>V;
		string B0,R0,Y0;
		if(R==0 && B==0 && O==0 && G==0){
			if(Y!=V){
				cout<<"IMPOSSIBLE"<<endl;
			}
			else{
				string ans;
				for(int i=0;i<Y;i++) ans+="YV";
				cout<<ans<<endl;
			}
			continue;
		}
		if(R==0 && Y==0 && V==0 && G==0){
			if(B!=O){
				cout<<"IMPOSSIBLE"<<endl;
			}
			else{
				string ans;
				for(int i=0;i<Y;i++) ans+="BO";
				cout<<ans<<endl;
			}
			continue;
		}
		if(Y==0 && B==0 && O==0 && V==0){
			if(R!=G){
				cout<<"IMPOSSIBLE"<<endl;
			}
			else{
				string ans;
				for(int i=0;i<Y;i++) ans+="RG";
				cout<<ans<<endl;
			}
			continue;
		}
		if(O!=0 && O>B-1){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(G!=0 && G>R-1){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if(V!=0 && V>Y-1){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		for(int i=0;i<O;++i) B0+="BO";
		B0 += "B";
		for(int i=0;i<G;++i) R0+="RG";
		R0 += "R";
		for(int i=0;i<V;++i) Y0+="YV";
		Y0 += "Y";
		B-=O;
		R-=G;
		Y-=V;
		N-= 2*(O+G+V);
		if(B>N/2 || R>N/2 ||Y>N/2){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		string tmp(N,' '),ans;
		bool ok = (R>Y);
		if(ok){
		for(int i=0;i<N;i+=2){
			if(R){
				tmp[i] = 'R';
				R--;
			}
			else{
				tmp[i] = 'Y';
				Y--;
			}
		}}
		else{
		for(int i=0;i<N;i+=2){
			if(Y){
				tmp[i] = 'Y';
				Y--;
			}
			else{
				tmp[i] = 'R';
				R--;
			}
		}}
		for(int i=1;i<N;i+=2){
			if(R){
				tmp[i] = 'R';
				R--;
			}
			else if(Y){
				tmp[i] = 'Y';
				Y--;
			}
			else{
				tmp[i] = 'B';
			}
		}
		bool cr = true, cb = true, cy = true;
		for(int i=0;i<N;++i){
			if(tmp[i]=='R' && cr){
				ans += R0;
				cr = false;
			}
			else if(tmp[i] == 'B' && cb){
				ans += B0;
				cb = false;
			}
			else if(tmp[i] == 'Y' && cy){
				ans += Y0;
				cy = false;
			}
			else{
				ans += tmp[i];
			}
		}
		cout<<ans<<endl;
    }
    return 0;
}


