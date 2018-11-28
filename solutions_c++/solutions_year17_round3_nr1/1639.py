#define _USE_MATH_DEFINES
#include<bits/stdc++.h>
using namespace std;
bool cmp(pair<double,double> a,pair<double,double> b){
	return a.first>b.first;
}
int main(){
	int t;
	cin>>t;
	for(int times=0;times<t;times++){
		int n,k;
		cin>>n>>k;
		pair<double,double> c[1005],c2[1005];
		for(int i=0;i<n;i++){
			cin>>c[i].second>>c[i].first;
			c[i].first*=c[i].second*2;
			c2[i].first=c[i].second;
			c2[i].second=c[i].first;
		}
		sort(c,c+n,cmp);
		/*for(int i=0;i<n;i++){
			cout<<c[i].second<<" "<<c[i].first<<endl;
		}*/
		
		double r=0;
		double h=0,maxh=0,maxr=0,maxa=0;
		for(int i=0,j=0;i<n;i++){
			//cout<<i<<" ";
			r=c[i].second;
			h+=c[i].first;
			j+=1;
			for(int id=0;id<n && j<k;id++){
				if(id==i)continue;
				if(c[id].second<=r){
					//cout<<id<<" ";
					h+=c[id].first;
					j++;
				}
			}
			//cout<<endl;
			if(j==k){
				if(r*r+h>maxa){
					maxa=r*r+h;
				}
			}
			r=0;
			h=0;
			j=0;
			//cout<<maxa<<endl;
		}
		double ans=(double)(maxa*M_PI);
		printf("Case #%d: %f\n",1+times,ans);
	}
	
	return 0;
}

