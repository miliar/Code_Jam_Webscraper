#include <bits/stdc++.h>
//#include <math.h>    work with doubles 18 significative cifras   round-mas cercano, floor-inferior, ceil-superior, trunc-truncar 
#define endl '\n'
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;
typedef long long ll ;
typedef vector<int> vi ;
struct alfa{
	long double x,y;
};
bool f(alfa a, alfa b){
	if(a.x<b.x)return 1;
	return 0;
}

int main() {
	//fast_io();	
	int t,t1;
	cin>>t;
	t1=t;
	while(t--){
		int n;
		vector<alfa> k;
		alfa xx;
		long double d,k1,v,s1,mini=1000000000000000000.0;
		cin>>d>>n;
		for(int i=0;i<n;i++){
			cin>>k1>>s1;
			xx.x=k1;
			xx.y=s1;
			k.push_back(xx);
		}
		sort(k.begin(),k.end(),f);
		
		for(int i=0;i<n;i++){
			k1=k[i].x;
			s1=k[i].y;
			v=(k1*s1)/(d-k1)+s1;
		//	if(v<=0)continue;
			if(v<mini)mini=v;
		}
		cout.precision(12);
		cout<<"Case #"<<t1-t<<": ";
	cout<<fixed<<mini<<endl;
		k.erase(k.begin(),k.end());
	}
	return 0;
}
