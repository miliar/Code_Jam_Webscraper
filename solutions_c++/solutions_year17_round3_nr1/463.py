#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
using namespace std;
int n,k;
vector<pair<long long,long long> >v;
bool orden(pair<long long,long long>a,pair<long long,long long>b){
	if(a.first!=b.first)return a.first>b.first;
	return a.second>b.second;
}


int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		printf("Case #%d: ",caso);
		long long dev=0;
		cin>>n>>k;
		v.clear();
		
		for(int i=0;i<n;i++){
			long long a,b;
			cin>>a>>b;
			v.push_back(make_pair(a,b));
		}
		
		sort(v.begin(),v.end(),orden);
		
		for(int i=0;i<n;i++){
			long long sum=(v[i].first*v[i].first)+2*v[i].first*v[i].second;
			vector<long long>prod;
			for(int j=i+1;j<n;j++)
				prod.push_back(v[j].first*v[j].second*2);
			
			if(prod.size()<k-1)continue;
			
			sort(prod.begin(),prod.end());
			reverse(prod.begin(),prod.end());
			
			for(int j=0;j<k-1;j++)
				sum+=prod[j];
			
			dev=max(dev,sum);
		}
		
		double ans=dev;
		ans=ans*acos(-1);
		printf("%.10lf\n",ans);
	}
		
	return 0;
}





