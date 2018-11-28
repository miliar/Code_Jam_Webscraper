#include <bits/stdc++.h>

using namespace std;

#define st first
#define nd second
#define pb push_back
typedef pair<int,int> ii;
typedef vector<ii> vii;

int t;

ofstream haha;

int main()
{
	freopen("a-small.out","w",stdout);
	//haha.open("a-small.out");
	//haha.open("a-large.out");
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++) {
		int n;
		double d,ans,k,s,t,max_t = 0.0;
		scanf("%lf %d",&d,&n);
		for(int i=0;i<n;i++) {
			scanf("%lf %lf",&k,&s);
			if(k<d) {
				double dis = d-k;
				double t = dis/s*1.0;
				if(t>max_t) max_t = t;
			} 
		}
		ans = d/max_t*1.0;
		printf("Case #%d: %.7lf\n",tc,ans);
		//haha << "Case #" << tc << ": " << ans << "\n";
	}
	//haha.close();
	fclose(stdout);
	return 0;
}