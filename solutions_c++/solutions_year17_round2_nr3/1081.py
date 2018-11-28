#include <bits/stdc++.h>

using namespace std;

int dist[111][111];
int n;

double ary[111];
vector<int> range,speed;


double min_time(int pos){
	if(pos==n-1)return 0;
	double &ret =ary[pos];
	if(ret==ret)return ret;
	ret = 1e100;
	int d = 0;
	for(int i=pos+1;i<n;i++){
		if(dist[i-1][i]==-1)break;
		d+=dist[i-1][i];
		if(d>range[pos])break;
		ret = min(ret, 1.0*d/speed[pos]+min_time(i));
		
	}
	return ret;
}

int main(void){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for(int t=1;t<=test;t++){
		int q;
		cin>>n>>q;
		range.resize(n);
		speed.resize(n);
		for(int i=0;i<n;i++)cin>>range[i]>>speed[i];
		memset(dist,0,sizeof(dist));
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++)cin>>dist[i][j];
		}
		vector<double> ans;
		for(int i=0;i<q;i++){
			int a,b;
			cin>>a>>b;
			memset(ary,-1,sizeof(ary));
			ans.push_back(min_time(a-1));
		}
		printf("Case #%d:",t);
		for(int i=0;i<ans.size();i++)printf(" %.10lf",ans[i]);
		printf("\n");
	}
	return 0;
}
