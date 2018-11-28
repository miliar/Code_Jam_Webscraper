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


int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		printf("Case #%d: ",caso);
		cin>>n>>k;
		double x;
		cin>>x;
		n++;
		double p[n];
		for(int i=0;i<n-1;i++)cin>>p[i];
		p[n-1]=1;
		sort(p,p+n);

		for(int i=1;i<n;i++){
			double dif=p[i]-p[i-1];
			if(dif*i<=x){
				x-=dif*i;
				for(int j=0;j<i;j++)
					p[j]=p[i];
			}else{
				for(int j=0;j<i;j++)
					p[j]+=x/i;
				break;
			}
		}
		
		double dev=1;
		for(int i=0;i<n;i++)
			dev*=p[i];
		printf("%.10lf\n",dev);
	}
	
		
	return 0;
}


