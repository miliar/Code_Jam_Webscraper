#include<bits/stdc++.h>
using namespace std;
const int maxn=1010;
int n;
int R,O,Y,G,B,V;
// O = R + Y
// G = Y + B
// V = B + R
int mp[255],pri[22];
char opp[255];
string calc(int n,int R,int O,int Y,int G,int B,int V){
	static char s[maxn];
	char la=0;
	mp['R']=0;
	mp['Y']=1;
	mp['B']=2;

	if(R<0||Y<0||B<0)
		return string("IMPOSSIBLE");
	for(int i=1;i<=n;i++){
		vector<pair<int,char> >vec;
		if(la!='R'&&R)vec.push_back({R,'R'});
		if(la!='Y'&&Y)vec.push_back({Y,'Y'});
		if(la!='B'&&B)vec.push_back({B,'B'});
		char c;
		if(vec.empty())
			return string("IMPOSSIBLE");
		auto cmp=[](pair<int,char>a,pair<int,char>b){
			if(a.first!=b.first)return a.first>b.first;
			return pri[mp[a.second]]>pri[mp[b.second]];
		};
		sort(vec.begin(),vec.end(),cmp);
		c=vec[0].second;
		la=c;
		s[i]=c;
//		cerr<<c;
		if(c=='R')R--;
		if(c=='Y')Y--;
		if(c=='B')B--;
	}
//	cerr<<endl;

	s[n+1]='\0';
	if(s[1]==s[n])
		return string("IMPOSSIBLE");
	else
		return string(s+1,s+1+n);
}

bool check(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]==s[(i+1)%s.length()])
			return false;
	}
	return true;
}


string update(string s){
	string g,v,o;
	g+=opp['G'];
	for(int i=0;i<G;i++){
		g+='G';
		g+=opp['G'];
	}
	v+=opp['V'];
	for(int i=0;i<V;i++){
		v+='V';
		v+=opp['V'];
	}
	o+=opp['O'];
	for(int i=0;i<O;i++){
		o+='O';
		o+=opp['O'];
	}

	for(int i=0;i<s.length();i++){
		if(s[i]==opp['G']){
			s.replace(i,1,g);
			break;
		}
	}
	for(int i=0;i<s.length();i++){
		if(s[i]==opp['V']){
			s.replace(i,1,v);
			break;
		}
	}
	for(int i=0;i<s.length();i++){
		if(s[i]==opp['O']){
			s.replace(i,1,o);
			break;
		}
	}
	return s;
}

bool special_case(){
	if(R==G&&R+G==n){
		for(int i=0;i<n;i++){
			putchar(i%2?'R':'G');
		}
		puts("");
		return true;
	}
	if(Y==V&&Y+V==n){
		for(int i=0;i<n;i++){
			putchar(i%2?'Y':'V');
		}
		puts("");
		return true;
	}
	if(B==O&&B+O==n){
		for(int i=0;i<n;i++){
			putchar(i%2?'B':'O');
		}
		puts("");
		return true;
	}
	return false;
}

void solve(){
	pri[0]=0;
	pri[1]=1;
	pri[2]=2;
	
	cin>>n>>R>>O>>Y>>G>>B>>V;


	if(special_case()){
		return ;
	}

	R-=G;
	Y-=V;
	B-=O;
//	cerr<<R<<" "<<Y<<" "<<B<<endl;
	do{
		string ans=calc(n-G*2-V*2-O*2,R,O,Y,G,B,V);
		if(ans!="IMPOSSIBLE"){
			ans=update(ans);
			printf("%s\n",ans.c_str());
//			if(!check(ans))assert(0);
			return;
		}
	}while(next_permutation(pri,pri+3));
//	cout<<n<<" "<<R<<" "<<Y<<" "<<B<<endl;
	puts("IMPOSSIBLE");
}

int main(){
	opp['R']='G';
	opp['G']='R';
	opp['Y']='V';
	opp['V']='Y';
	opp['B']='O';
	opp['O']='B';
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		printf("Case #%d: ",t);
		solve();
	}
	return 0;
}
