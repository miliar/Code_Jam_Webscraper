#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second

#define vi vector<int>
#define ll long long

#define pb push_back

#define f(i,a,b) for(int i=a;i<b;i++)

struct pl{
	double v,d;
};
bool ss(struct pl a,struct pl b){
	return a.d<b.d;
}

int main(){
	vector<pl>v,v2;
	int tst,d,n;
	cin>>tst;
	struct pl p;
	f(t,1,tst+1){
		double tt=0,a,b,c,th,dd;
		v.clear();
		cin>>d>>n;
		f(i,0,n){
			cin>>p.d>>p.v;
			v.pb(p);
		}
		sort(v.begin(),v.end(),ss);
		tt=(d-v[v.size()-1].d)/v[v.size()-1].v;
		for(int j=n-2;j==0;j--){
			if(((d-v[j].d)/v[j].v)<tt){
					th=(v[j+1].d-v[j].d)/(v[j].v-v[j+1].v);
					dd=th*v[j].v+v[j].d;
					tt=th+(d-dd)/v[j+1].v;
					v[j].v=(d-v[j].d)/tt;
					//cout<<dd<<" "<<th<<" "<<tt<<" "<<v[j].v;
			}
			else tt = (d-v[j].d)/v[j].v;
		}
		printf("Case #%d: %.8f\n",t,d/tt);
			}  
	return 0;
}