# include <iostream>
# include <string.h>
using namespace std;

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for (int j = 0; j < t; j++){
		int d,n;
		cin>>d>>n;
		double x[n+10][2];
		double max = 0;
		for (int i = 0; i < n; i++){
			cin>>x[i][0]>>x[i][1];
			double dis = d - x[i][0];
			double time = dis/x[i][1];
			if (time > max){
				max = time;
			}
		}
		double ans = d/max;
		printf("Case #%d: ",j+1);
		printf("%.6f\n",ans);
		//cout<<ans<<endl;
	}
	return 0;
}
