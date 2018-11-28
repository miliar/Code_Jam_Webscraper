#include<bits/stdc++.h>
using namespace std;

int sisa[5];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("haha.txt","w",stdout);
	int t; cin>>t;
	
	for(int tmp=1;tmp<=t;tmp++){
		int n,k; cin>>n>>k;
		memset(sisa,0,sizeof(sisa));
	//	cout<<"haha "<<n<<k<<"\n";
		for(int sem=0;sem<n;sem++){
			int a; cin>>a;
			sisa[a%k]++;
		}
		if(k==2){
			int tamb = (sisa[1]+1)/2;
			int jawab = sisa[0] + tamb;
			printf("Case #%d: %d\n",tmp,jawab);
		}else if(k==3){
			int sel = abs(sisa[1] - sisa[2]) + 2;
			int jawab = sisa[0] + min(sisa[1],sisa[2]) + sel/3;
			printf("Case #%d: %d\n",tmp,jawab);
		}
	}
	
}
