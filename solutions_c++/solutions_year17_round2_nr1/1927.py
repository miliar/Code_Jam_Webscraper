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
#include <stdlib.h> 
using namespace std;
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		double D;
		int N;
		cin>>D>>N;
		
		double pos[N];
		double vel[N];
		double maxvel=0;
		
		for(int i=0;i<N;i++){
			cin>>pos[i]>>vel[i];
			maxvel=max(maxvel,vel[i]);
		}
		
		double lo=0;double hi=1e+20;
		
		for(int i=0;i<100;i++){
			double me=(lo+hi)/2;
			double t=D/me;
			bool ok=1;
			for(int j=0;j<N;j++){
				double t2=(D-pos[j])/vel[j];
				if(t<t2){
					ok=0;
				}
			}
			
			if(ok)
				lo=me;
			else
				hi=me;
		}
		
		printf("%.10lf\n",lo);
	}
	
	return 0;
}


