#include <bits/stdc++.h>
#define F first
#define S second
#define X real()
#define Y imag()
using namespace std;
typedef long long ll;
typedef long double ld;

string s[30];
string os[30];

int can(int ra, int ca, int rb, int cb, char c){
	for (int i=ra;i<=rb;i++){
		for (int ii=ca;ii<=cb;ii++){
			if (s[i][ii]!=c){
				if (s[i][ii]!='?') return 0;
			}
		}
	}
	return 1;
}

void use(int ra, int ca, int rb, int cb, char c){
	for (int i=ra;i<=rb;i++){
		for (int ii=ca;ii<=cb;ii++){
			s[i][ii]=c;
		}
	}
}

int miR[30];
int maR[30];
int miC[30];
int maC[30];
int u[30];

void solve(){
	int r,c;
	cin>>r>>c;
	int f=0;
	for (int i=0;i<r;i++){
		cin>>s[i];
		os[i]=s[i];
		for (int ii=0;ii<c;ii++){
			if (s[i][ii]!='?') f=1;
		}
	}
	if (!f) s[0][0]='A';
	for (int i=0;i<30;i++){
		miR[i]=r-1;
		maR[i]=0;
		miC[i]=c-1;
		maC[i]=0;
		u[i]=0;
	}
	for (int i=0;i<r;i++){
		for (int ii=0;ii<c;ii++){
			if (s[i][ii]!='?'){
				miR[s[i][ii]-'A']=min(miR[s[i][ii]-'A'], i);
				maR[s[i][ii]-'A']=max(maR[s[i][ii]-'A'], i);
				miC[s[i][ii]-'A']=min(miC[s[i][ii]-'A'], ii);
				maC[s[i][ii]-'A']=max(maC[s[i][ii]-'A'], ii);
			}
		}
	}
	for (int i=0;i<r;i++){
	for (int ii=0;ii<c;ii++){
	if (s[i][ii]!='?'&&u[s[i][ii]-'A']==0){
		char ch=s[i][ii];
		u[ch-'A']=1;
		int ra=miR[ch-'A'];
		int rb=maR[ch-'A'];
		int ca=miC[ch-'A'];
		int cb=maC[ch-'A'];
		assert(can(ra, ca, rb, cb, ch));
		use(ra, ca, rb, cb, ch);
	}
	}
	}
	for (int i=0;i<r;i++){
	for (int ii=0;ii<c;ii++){
	if (s[i][ii]!='?'&&u[s[i][ii]-'A']==1){
		char ch=s[i][ii];
		u[ch-'A']=2;
		int ra=miR[ch-'A'];
		int rb=maR[ch-'A'];
		int ca=miC[ch-'A'];
		int cb=maC[ch-'A'];
		assert(can(ra, ca, rb, cb, ch));
		while (ca>0&&can(ra, ca-1, rb, cb, ch)){
			ca--;
		}
		while (ra>0&&can(ra-1, ca, rb, cb, ch)){
			ra--;
		}
		while (cb+1<c&&can(ra, ca, rb, cb+1, ch)){
			cb++;
		}
		while (rb+1<r&&can(ra, ca, rb+1, cb, ch)){
			rb++;
		}
		assert(can(ra, ca, rb, cb, ch));
		use(ra, ca, rb, cb, ch);
	}
	}
	}
	for (int i=0;i<r;i++){
		for (int ii=0;ii<c;ii++){
			assert(s[i][ii]!='?');
		}
	}
	cout<<endl;
	for (int i=0;i<r;i++){
		cout<<s[i]<<endl;
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++){
		cout<<"Case #"<<tc<<": ";
		solve();
	}
}