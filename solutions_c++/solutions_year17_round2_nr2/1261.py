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

string getRYB(int R, int Y, int B){
	if(R<0 || Y<0 || B<0)
		return "";
	int cnt = (R+Y+B)/2;
	if(R>cnt || Y>cnt || B>cnt)
		return "";
	string ret = "";
	int poss[3] = {1,1,1};
	int arr[3]; arr[0] = R;arr[1] = Y;arr[2] = B;
	char val[3] = {'R','Y','B'};
	int firstChar[3] = {-1,-1,-1};
	REP(ind, (R+Y+B)){
		int maxInd = -1;
		REP(i,3) if(poss[i] && (maxInd==-1 || arr[maxInd]<arr[i] || (arr[maxInd]==arr[i] && firstChar[i]==0))) maxInd = i;	
		REP(i,3) poss[i] = 1;
		poss[maxInd] = 0;
		arr[maxInd]--;
		if(ind==0)
			firstChar[maxInd] = 0;
		ret = ret + val[maxInd];
	}
	return ret;
}
string update(string s, int cnt, int type){
	if(cnt==0) return s;
	char val[3] = {'R','Y','B'};
	char val1[3] = {'G','V','O'};
	string prev = "";
	for(int i=0;i<s.length();i++){
		if(s[i]==val[type]){
			string s2 = "";
			while(cnt--)
				s2 = (s2 + val[type]) + val1[type];
			s2 = s2 + val[type];
			if(i==s.length()-1)
				return (prev + s2);
			else 
				return (prev + s2 + s.substr(i+1,s.length()-(i+1)));
		}
		prev = prev + s[i];
	}
	return s;
}
void solve(){
	int n,R,O,Y,G,B,V;
	s(n);s(R);s(O);s(Y);s(G);s(B);s(V);
	string s = getRYB(R-G,Y-V,B-O);
	if(R==G && n==(R+G)) {
		string s=""; REP(i,R) s = s + "RG"; cout<<s<<endl; return;
	}
	if(B==O && n==(B+O)) {
		string s=""; REP(i,B) s = s + "BO"; cout<<s<<endl; return;
	}
	if(Y==V && n==(Y+V)) {
		string s=""; REP(i,Y) s = s + "YV"; cout<<s<<endl; return;
	}
	if(s.length()==0)
		cout<<"IMPOSSIBLE"<<endl;
	else {
		s = update(s,O,2);
		s = update(s,G,0);
		s = update(s,V,1);
		cout<<s<<endl;
	}
}
int main()
{
	int t;
	s(t);
	REP(tt,t){
		cout<<"Case #"<<tt+1<<": ";
		solve();
	}
    return 0;
}
