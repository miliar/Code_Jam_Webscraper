#include<bits/stdc++.h>
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t;
	cin>>t;
	for(int tmp=0;tmp<t;tmp++){
		int d,n;
		cin>>d>>n;
		double time = 0;
		for(int sem=0;sem<n;sem++){
			int k,s;
			cin>>k>>s;
			double now = (double) (d-k)/s;
			if(now>time) time = now;
		}
		printf("Case #%d: %.6lf\n",tmp+1,d/time);
	}	
}

