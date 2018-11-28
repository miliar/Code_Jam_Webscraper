#include<bits/stdc++.h>
using namespace std;
int main(){
freopen("A-large.in","r",stdin);
    freopen("data.out","w",stdout);
	double loc[1005],sp[1005];
	int t, nt;
	cin>>t;
	for(int nt=1;nt<=t;nt++){
		long long int d, n;
		cin>>d>>n;
        double max = 100000000000000, p;
        for(int i=0;i<n;i++){
            cin>>loc[i]>>sp[i];
            if(max>sp[i]){
                p = d*sp[i]/(d-loc[i]);
                if(p<max && p>0)max=p;
            }
        }

		cout<<"Case #"<<nt<<": "<<fixed<<setprecision(6)<<max<<endl;	
	}
	return 0;
}
