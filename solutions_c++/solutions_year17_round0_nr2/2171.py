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
	ofs.open("D:\\tomo\\Programming\\GCJ\\GCJ2017 B-2.txt");
	lint n;
	cin>>n;
	rep(i,0,n){
		lint a,a2,s[50]={},s1[50]={};
		cin>>a;
		a2=a;
		int sizes=0;
		while(a>=1){
			s1[sizes]=a%10;
			a/=10;
			sizes++;
		}
		rep(j,0,sizes){
			s[j]=s1[sizes-1-j];
		}
		int flag=0,equal=0;
		rep(k,0,sizes-1){
			if(s[k]<s[k+1]){
				flag=k+1;
				equal=k+1;
			}
			else if(s[k]==s[k+1]){
				equal=k+1;
			}
			else break;
		}
		ofs<<"Case #"<<i+1<<": ";
		if(equal==(sizes-1))ofs<<a2<<endl;
		else if(flag==(sizes-1))ofs<<a2<<endl;
		else{
			int j;
			rep(j,0,flag){
				ofs<<s[j];
			}
			if(s[flag]!=1)ofs<<s[flag]-1;
			else if(s[flag]==1&&flag!=0)ofs<<0;
			rep(j,flag+1,sizes){
				ofs<<'9';
			}
			ofs<<endl;
		}
	}

return 0;
}