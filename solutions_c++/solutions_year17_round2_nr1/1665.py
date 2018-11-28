#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
using namespace std;
int main(){
	string fileName="A-large";
	freopen((fileName+".in").c_str(),"r",stdin);
	freopen((fileName+".out").c_str(),"w",stdout);
	int nn;
	cin>>nn;
	int ii=0;
	while(ii<nn){
		cout<<"Case #"<<ii+1<<": ";
		long long d;
		int n;
		cin>>d>>n;
		double ans=19970822000000.0;
		for(int i=0;i<n;i++){
			long long tempd;
			double tempv;
			cin>>tempd>>tempv;
			double tempans;
			tempans=(d*tempv/(d-tempd));
			if(ans>tempans)ans=tempans;
		} 
		printf("%.6lf\n",ans);

		ii++;
	}
}


