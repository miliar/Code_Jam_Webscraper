#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <set>
#include <algorithm>
#include <cctype>
#define DN 1000
using namespace std;

int T, n;
string s,rs;
int has[512],sol,fr[512];
char cand[]={'o','g','v','r','y','b'};

int okc(char a, char b) {
	return (has[a]&has[b])==0;
}

void bk(int p,int r,int y,int b) {
	if(sol) return;
	if(p==n) {

		if(okc(s.front(),s.back())) {
			sol=1;
			rs=s;
		}
		return;
	}
	vector<pair<int,char> >v;
	v.push_back(make_pair(r,'r'));
	v.push_back(make_pair(y,'y'));
	v.push_back(make_pair(b,'b'));
	sort(v.rbegin(),v.rend());
	for(auto i:v) {
		for(int j=0; j<6; ++j) if((has[cand[j]]&has[i.second]) && fr[cand[j]] && (!s.size() || okc(s.back(), cand[j]))) {
			--fr[cand[j]];
			s+=cand[j];
			if(i.second=='r') bk(p+1,r-1,y,b);
			else if(i.second=='y') bk(p+1,r,y-1,b);
			else bk(p+1,r,y,b-1);
			s.pop_back();
			++fr[cand[j]];
		}
	}
}

int main() {
	ifstream f("b.txt");
	ofstream g("b.out");
	f>>T;
	has['r']=1; has['y']=2; has['b']=4;
	has['o']=has['r']+has['y'];
	has['g']=has['y']+has['b'];
	has['v']=has['r']+has['b'];
	for(int t=1; t<=T; ++t) {
		sol=0;
		f>>n>>fr['r']>>fr['o']>>fr['y']>>fr['g']>>fr['b']>>fr['v'];
		int r=fr['r']+fr['o']+fr['v'],y=fr['y']+fr['o']+fr['g'],b=fr['b']+fr['g']+fr['v'];
		
		//cout<<n<<' '<<r<<' '<<y<<' '<<b<<'\n';
		if(r>n/2 || y>n/2 || b>n/2) rs="IMPOSSIBLE";
		if(!rs.size()) bk(0,r,y,b);
		for(int i=0; i<rs.size(); ++i) rs[i]=toupper(rs[i]);
		if(!rs.size()) rs="IMPOSSIBLE";
		
		g<<"Case #"<<t<<": ";
		g<<fixed<<setprecision(9)<<rs;
		g<<'\n';
		s.clear();
		rs.clear();
	}
}