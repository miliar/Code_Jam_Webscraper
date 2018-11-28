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
	ofs.open("D:\\tomo\\Programming\\GCJ\\GCJ2017 C-3.txt");
	lint t;
	cin>>t;
	rep(i,0,t){
		lint n,k;
		cin>>n>>k;
		lint n2=n,k2=(k+1),k3=k,cnt=0;
		while(k2>=1){
			k2/=2;
			cnt++;
		}
		cnt--;
		lint a=1;
		rep(j,0,cnt)a*=2;
		a--;
		if(k3==a)a=((a+1)/2-1);
		k3-=a;
		n2-=a;
		lint c;
		lint rest=n2%(a+1);
		lint b=(n2-rest)/(a+1);
		if(k3<=rest)c=(b+1);
		else c=b;
		ofs<<"Case #"<<i+1<<": ";
		if(c%2==1){
			ofs<<(c-1)/2<<" "<<(c-1)/2<<endl;
		}
		else{
			ofs<<c/2<<" "<<c/2-1<<endl;
		}

	}

return 0;
}