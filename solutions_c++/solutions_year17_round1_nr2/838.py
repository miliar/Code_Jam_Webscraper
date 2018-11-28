#include <bits/stdc++.h>

using namespace std;

int r[55];
int q[55][55];
int L[55][55];
int R[55][55];

int pos[55];

int n,p;

bool debug = 0;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		memset(pos,0,sizeof(pos));
		cas++;	
		cin>>n>>p;


		for(int i=0;i<n;i++){
			cin>>r[i];
		}

		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				cin>>q[i][j];
			}
			sort(q[i],q[i] + p);
		}
		
		int ans = 0;

		
		for(int i=0;i<n;i++){
			if(debug)cout<<"i = "<<i<<endl;
			for(int j=0;j<p;j++){
				if(debug)cout<<"		j = "<<j;
				int Time = q[i][j] / r[i];

				L[i][j] = Time + 1;
				R[i][j] = Time;
				for(int k = Time;;k--){
					if(r[i]*k*0.9<=q[i][j] && r[i]*k*1.1>=q[i][j]){
						L[i][j] = k;
					}else{
						break;
					}
				}
				for(int k = Time+1;;k++){
					if(r[i]*k*0.9<=q[i][j] && r[i]*k*1.1>=q[i][j]){
						R[i][j] = k;
					}else{
						break;
					}
				}
				if(debug)cout<<"  "<<L[i][j]<<" "<<R[i][j]<<endl;
			}
		}

		for(int k=1;k<=1000000;k++){
			bool ok = 1;
			for(int i=0;i<n;i++){
				if(pos[i]>=p){
					goto outer;
				}
				while(pos[i]<p-1 && (R[i][pos[i]] < k  || L[i][pos[i]] > R[i][pos[i]])  ){
					pos[i] ++;
				}

				if(L[i][pos[i]] <= k && R[i][pos[i]] >= k){
					// ok
					
				}else{
					ok = 0;
				}
			}
			if(ok){
				if(debug){
					cout<<"k = "<<k<<" ok !"<<endl;
				}
				for(int i=0;i<n;i++){
					pos[i]++;
				}
				k--;
				ans++;
			}
		}
			
		outer:

		printf("Case #%d: ",cas);

		cout<<ans<<endl;
	}
	return 0;
}
