#include <bits/stdc++.h>
#define ft first
#define sd second
#define mp make_pair
#define MAX 100010
#define pb push_back
#define len length
using namespace std;
typedef long long int lli;
typedef pair<lli,lli> pll;
typedef pair<int,int> pii;
typedef map<lli,lli> mll;
typedef map<int,int> mii;
typedef priority_queue<lli, vector<lli> > pqllix;

const int M=1e9+7;
// char s[30][30];
void solve() {
	int r,c,i,j,k;
	cin>>r>>c;
	string s[r];
	for(i=0;i<r;i++) {
		cin>>s[i];
	}
	char c1='*';
	for(i=0;i<r;i++) {
		for(j=0,c1='*';j<c;j++) {
			if (s[i][j]!='?') {
				c1=s[i][j];
			} else if (c1!='*') {
				s[i][j]=c1;
			}  
		}
		for(j=c-1,c1='*';j>=0;j--) {
			if (s[i][j]!='?') {
				c1=s[i][j];
			} else if (c1!='*') {
				s[i][j]=c1;
			}
		}
	}

	for(i=0;i<r;i++) {
		if (s[i][0]=='?') continue;
	for(int m=i;m>0;m--) {
	for(j=m-1;j>=0 && j+1<r && s[j][0]=='?';j--) {
		for(k=0;k<c;k++) {
			s[j][k]=s[j+1][k];
		}
	}
}
}

	for(i=r-1;i>=0;i--) {
		if (s[i][0]=='?') continue;
		for(int m=i;m<r;m++) {
	for (j=m+1;j>=1 && j<r && s[j][0]=='?';j++) {
		for(k=0;k<c;k++) {
			s[j][k]=s[j-1][k];
		}
	}
}
	
}

	for(i=0;i<r;i++) {
		cout<<s[i]<<'\n';
		// cout<<'\n';
	}


}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<":\n";
		solve();
	}
	return 0;
}
