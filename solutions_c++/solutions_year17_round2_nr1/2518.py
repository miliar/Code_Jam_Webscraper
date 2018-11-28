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
	ofstream ofs("D:\\tomo\\Programming\\GCJ\\Round1B\\Alarge.txt");
	int t;
	cin>>t;
	rep(i,0,t){
		double k[1000],s[1000];
		lint d,n;
		cin>>d>>n;
		rep(j,0,n){
			cin>>k[j]>>s[j];
		}
		double max=0;
		rep(j,0,n){
			if(((d-k[j])/s[j])>max)max=((d-k[j])/s[j]);
		}
		ofs<<"Case #"<<i+1<<": "<<fixed<<setprecision(10)<<d/max<<endl;
	}

return 0;
}