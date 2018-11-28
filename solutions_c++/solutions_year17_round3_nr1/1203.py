#include<iostream> 
#include<algorithm>
#include<stdio.h>
#include<vector>
using namespace std;
typedef pair<double,double>pii;
void Gao(){
	int T;
	int n,k;
	//scanf("%d",&T);
	cin>>T;
	for(int t=1;t<=T;t++){
		double ans =0.0;
		int n,k;
		cin>>n>>k;
		vector<pii>a;
		for(int i=0;i<n;i++){
			double x,y;
			cin>>x>>y;
			a.push_back(make_pair(x,y));
		} 
		sort(a.begin(),a.end());
		//cout<<"works"<<endl;
		
		double pi = 3.1415926535898;
		for(int tt=0;tt<n;tt++){
			vector<double>tem;
			double di=pi*a[tt].first*a[tt].first;
			double temsum=di+2.0*pi*a[tt].first*a[tt].second;
			for(int i=0;i<tt;i++){
				tem.push_back(-1.0*2*pi*a[i].second*a[i].first);
			}
			int tnum=1;
			sort(tem.begin(),tem.end());
			//if(tem.size()<(k-1)){
			//	continue;
				if(tem.size()!=0){
					for(int i=0;(i<(k-1))&&(i<tem.size());i++){
						temsum+=-1.0*tem[i];
						tnum++;
					}
				}
			//}
			if(temsum>ans&&tnum==k){
				ans= temsum;
			}
			//cout<<tt<<"??"<<endl;
		}
		printf("Case #%d: %.9lf\n",t,ans);
	}
}
int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("al.out","w",stdout);
	Gao();
	return 0;
}
