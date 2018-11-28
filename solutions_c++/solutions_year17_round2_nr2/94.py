#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F first
#define S second
#define X real()
#define Y imag()

string create(int r, int o, int y, int g, int b, int v) {
	string s="";
	if (y==0 && b==0) {
		for (int i=0;i<r;i++) {
			s.push_back('R');
			s.push_back('G');
		}
		return s;
	}
	if (r==0 && b==0) {
		for (int i=0;i<y;i++) {
			s.push_back('Y');
			s.push_back('V');
		}
		return s;
	}
	if (r==0 && y==0) {
		for (int i=0;i<b;i++) {
			s.push_back('B');
			s.push_back('O');
		}
		return s;
	}
	int si=max(max(r-g,y-v),b-o);
	int rlo=0;
	int rhi=r-g;
	int ylo=0;
	int yhi=y-v;
	int blo=0;
	int bhi=b-o;
	if (si!=b-o) {
		blo+=si-(b-o);
		bhi+=si-(b-o);
		if (si>r-g) {
			blo--;
			bhi--;
		}
	} else {
		ylo+=si-(y-v);
		yhi+=si-(y-v);
	}
	bool gdra=false;
	bool vdra=false;
	bool odra=false;
	for (int i=0;i<si;i++) {
		if (i>=rlo && i<rhi) {
			if (!gdra) {
				for (int ii=0;ii<g;ii++) {
					s.push_back('R');
					s.push_back('G');
				}
				gdra=true;
			}
			s.push_back('R');
		}
		if (i>=ylo && i<yhi) {
			if (!vdra) {
				for (int ii=0;ii<v;ii++) {
					s.push_back('Y');
					s.push_back('V');
				}
				vdra=true;
			}
			s.push_back('Y');
		}
		if (i>=blo && i<bhi) {
			if (!odra) {
				for (int ii=0;ii<o;ii++) {
					s.push_back('B');
					s.push_back('O');
				}
				odra=true;
			}
			s.push_back('B');
		}
	}
	return s;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++) {
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>y>>g>>b>>v;
		int rr=r-g;
		int yy=y-v;
		int bb=b-o;
		bool ok=true;
		if (rr<0) ok=false;
		if (yy<0) ok=false;
		if (bb<0) ok=false;
		if (rr+yy<bb) ok=false;
		if (rr+bb<yy) ok=false;
		if (bb+yy<rr) ok=false;
		if (rr==0 && r>0) {
			if (y>0 || b>0) ok=false;
		}
		if (yy==0 && y>0) {
			if (r>0 || b>0) ok=false;
		}
		if (bb==0 && b>0) {
			if (r>0 || y>0) ok=false;
		}
		cout<<"Case #" <<tc<<": ";
		if (ok) {
			string s = create(r,o,y,g,b,v);
			assert((int)s.size()==n);
			for (int i=0;i<n;i++) {
				assert(s[i]!=s[(i+1)%n]);
			}
			cout<<s<<endl;
		}
		else cout<<"IMPOSSIBLE"<<endl;
	}
}
