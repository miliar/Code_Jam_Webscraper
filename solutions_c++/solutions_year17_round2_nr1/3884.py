#include <bits/stdc++.h>
using namespace std;
struct T{
	long double k,s;
};
bool cmp(T a,T b){
	return a.k<b.k;
}

int main(){
	freopen("A-large.in", "r", stdin);
  	freopen("asdasd.out", "w", stdout);
	int t,n;
	long double D;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>D>>n;
		vector<T> v(n);
		for(int i=0;i<n;i++){
			cin>>v[i].k>>v[i].s;
		}
		sort(v.begin(),v.end(),cmp);
		int w[n];
		double f[n];
		
		memset(w,-1,sizeof(w));
		memset(f,0.0,sizeof(f));
		for(int i=0;i<n;i++){
			int id=-1;
			double di=D;
			for(int j=1;j<n;j++){
				if(v[i].s>v[j].s){
					double ti=(v[j].k-v[i].k)/(v[i].s-v[j].s);
					double dx=v[i].k+v[i].s*ti;
					if(dx<di){
						di=dx;
						id=j;
					}
				}
			}
			w[i]=id;
			f[i]=di;
		}
		double temp=0.0,dis=v[0].k;
		for(int i=0;i<n;){
			if(w[i]==-1){
				temp+=(D-dis)/v[i].s;
				break;
			}else{
				temp+=(f[i]-dis)/v[i].s;
				dis=f[i];
				i=w[i];
			}
		}
		long double ans=D/temp;
		cout<<"Case #"<<k<<": ";
		printf("%.6Lf\n",ans);
	}
	return 0;
}
/*
1000000000
1000000000
*/