#include<bits/stdc++.h>

#define s(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)

#define MP           make_pair
#define PB           push_back
#define REP(i, n)    for(int i = 0; i < n; i++)
#define INC(i, a, b) for(int i = a; i <= b; i++)
#define DEC(i, a, b) for(int i = a; i >= b; i--)
#define CLEAR(a)     memset(a, 0, sizeof a)

using namespace std;

typedef long long          LL;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int, int>     II;
typedef vector<II>         VII;

char inp[26][26];

bool fillrow(int r, int c){
	bool f = false;
	for(int j=0;j<c;j++){
		if(inp[r][j]!='?'){
			f = true;
			for(int i=j-1;i>=0 && inp[r][i]=='?';i--)
				inp[r][i] = inp[r][j];
			for(int i=j+1;i<c && inp[r][i]=='?';i++)
				inp[r][i] = inp[r][j];
		}
	}
	return f;
}
void copy(int r1, int r2, int c){
	for(int i=0;i<c;i++)
		inp[r2][i] = inp[r1][i];
}
void solve(){
	int r,c;
	cin>>r>>c;
	REP(i,r)
		ss(inp[i]);
	int prev = -1;
	for(int row=0;row<r;row++){
		if(fillrow(row,c))
			prev = row;
		else {
			if(inp[row][0]=='?' && prev!=-1){
				copy(prev,row,c);
			}
		}
	}
	prev = -1;
	for(int row=r-1;row>=0;row--){
		if(fillrow(row,c))
			prev = row;
		else {
			if(inp[row][0]=='?' && prev!=-1){
				copy(prev,row,c);
			}
		}
	}
	for(int i=0;i<r;i++)
		printf("%s\n",inp[i]);
}
int main()
{
	int t;
	s(t);
	REP(tt,t){
		cout<<"Case #"<<tt+1<<":"<<endl;
		solve();
	}
    return 0;
}
