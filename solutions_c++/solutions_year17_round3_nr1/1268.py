#include<bits/stdc++.h>
using namespace std;

vector<pair<double,double> >V;
vector<double>T;

int main(){
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,tt,n,k,i,r,h;
	double mpie=3.14159265358979323846;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt){
		scanf("%d %d",&n,&k);
		for(i=0;i<n;++i){
			scanf("%d %d",&r,&h);
			V.push_back(make_pair((double)r,(double)h));
		}
		sort(V.rbegin(),V.rend());
		double fans=0;
		for(int j=0;j<n;++j){
			if(j+k-1>=n) break;
			double ans=0;
			ans=ans+(V[j].first*V[j].first);
			ans=ans+(2*V[j].first*V[j].second);
			for(i=j+1;i<n;++i){
				T.push_back((2*V[i].first*V[i].second));
			}
			sort(T.rbegin(),T.rend());
			for(i=0;i<k-1;++i){
				ans=ans+T[i];
			}
			
			
			/*
			double ans=0;
			int cnt=0;
			for(i=j;i<(j+k)&&i<n;++i){
				++cnt;
				if(i==j){
					ans=ans+(V[i].first*V[i].first);
				}
				ans=ans+(2*V[i].first*V[i].second);
			}
			*/
			fans=fmax(ans,fans);
			T.clear();
		}
		/*
		for(i=0;i<k;++i){
			if(i==0){
				ans=ans+(V[i].first*V[i].first);
			}
			ans=ans+(2*V[i].first*V[i].second);
		}
		*/
		fans=fans*mpie;
		printf("Case #%d: ",tt);
		cout<<setprecision(30)<<fans<<endl;
		//printf("%lf\n",fans);
		V.clear();
	}
	return 0;
}
