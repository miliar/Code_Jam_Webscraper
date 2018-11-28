#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iomanip>
#include<fstream>

#define rep(i,a,N) for(int i=0+a;i<N;i++)
#define lint long long int
#define SIZE 100005
#define pb push_back
#define MP make_pair

using namespace std;

int main(){
	ofstream ofs;
	ofs.open("D:\\tomo\\Programming\\GCJ\\GCJ2017 A-2.txt");
	lint n;
	cin>>n;
	rep(i,0,n){
		string s;
		lint a,cnt=0,ok=0;
		cin>>s>>a;
		rep(j,0,s.size()-a+1){
			if(s[j]=='-'){
				cnt++;
				rep(k,0,a){
					if(s[j+k]=='-')s[j+k]='+';
					else s[j+k]='-';
				}
			}
		}
		rep(l,0,s.size()){
			if(s[l]=='-')ok=1;
		}
		if(ok==0){
			ofs<<"Case #"<<i+1<<": "<<cnt<<endl;
		}
		else{
			ofs<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
		}
		ok=0;
	}
return 0;
}