#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < int(b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define D(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
    cin.sync_with_stdio(false);
	int t; cin>>t;
	int Case = 1;
	while(t--) {
		cout<<"Case #"<<Case++<<": ";
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		int mx = max(r,max(y,b));
		char last;
		if(r==mx){last = 'R';--r;}
		else if(y==mx){last = 'Y';--y;}
		else if(b==mx){last = 'B';--b;}
		string output = ""; output += last;
		char first = last;
		bool possible = true;
		while(true){
			if(last=='Y'){
				if(r==0&&b==0) possible = false;
				if(r<b||(r==b&&first=='B')){last = 'B';--b;}
				else {last = 'R';--r;}
			}else
			if(last=='B'){
				if(r==0&&y==0) possible = false;
				if(r<y||(r==y&&first=='Y')) {last = 'Y';--y;}
				else {last = 'R';--r;}
			}else
			if(last=='R'){
				if(y==0&&b==0) possible = false;
				if(y<b||(y==b&&first=='B')){last = 'B';--b;}
				else{last = 'Y';--y;}
			}
			output+=last;
			if(!possible||r+y+b==0) break;
			/*if(y+r+b==2){
				if(r==1&&b==1){
					if((last=='B'&&first!='B')||(last!='R'&&first=='R')) output += "RB";
					else if((last=='R'&&first!='R')||(last!='B'&&first=='B')) output += "BR";
					else if(last=='Y'&&first=='Y') output += "BR";
					else possible = false;
				}else
				if(r==1&&y==1){
					if((last=='Y'&&first!='Y')||(last!='R'&&first=='R')) output += "RY";
					else if((last=='R'&&first!='R')||(last!='Y'&&first=='Y')) output += "YR";
					else if(last=='B'&&first=='B') output += "YR";
					else possible = false;
				}else
				if(y==1&&b==1){
					if((last=='B'&&first!='B')||(last!='Y'&&first=='Y')) output += "YB";
					else if((last=='Y'&&first!='Y')||(last!='B'&&first=='B')) output += "BY";
					else if(last=='R'&&first=='R') output += "BY";
					else possible = false;
				}else
					possible = false;
				break;
			}*/
		}
		if(possible&&last!=first){
			cout<<output<<endl;
		}else{
			cout<<"IMPOSSIBLE"<<endl;
		}
	}
}