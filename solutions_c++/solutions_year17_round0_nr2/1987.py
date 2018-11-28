/*ckpeteryu Code Jam 2017 QR - Problem B Tidy Numbers*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long unsigned int

int nt;
LL N;

//AC-small
string brute(){
	stringstream ss;
	string s;
	for(LL i=N;i>=1;i--){
		ss<<i;
		s=ss.str();
		//cout<<s<<endl;
		ss.str(string());
		int len=s.length();
		bool good=true;
		FOR(i,1,len){
			if(s[i-1]>s[i])
				good=false;
		}
		if(good)
			break;
	}
	return s;
}

string solve(){
	stringstream ss;
	string s;
	ss<<N;
	s=ss.str();
	int len=s.length();
	bool good=true;
	while(1){		
		int pos=-1;
		FOD(i,len-1,1){
			if(s[i-1]>s[i]){
				good=false;
				pos=i-1;
				break;
			}
		}
		if(pos!=-1){			
			s[pos]-=1;
			FOR(i,pos+1,len){
				s[i]='9';
			}
		}else
			break;
	}
	ss.str(string());	
	return s.substr(s.find_first_not_of("0"));
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	scanf("%d",&nt);
	FOE(k,1,nt){
		scanf("%llu",&N);				
		//printf("Case #%d: %s\n",k,brute().c_str());//AC-small
		printf("Case #%d: %s\n",k,solve().c_str());
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}