#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef struct pa{
	int min;
	int max;
} pa;

bool big(pa a, pa b){
	if(a.min<b.min) return true;
	if(a.min==b.min&&a.max<=b.max) return true;
	return false;
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		int n,p;
		int i,j;
		int pack[50];
		int a[50][50];
		vector<pa> b[50];
		cin>>n>>p;
		for(i=0;i<n;i++){
			cin>>pack[i];
		}
		pa temp;
		for(i=0;i<n;i++){
			for(j=0;j<p;j++){
				cin>>a[i][j];
				temp.min=(10*a[i][j]-1)/(11*pack[i])+1;
				temp.max=10*a[i][j]/(9*pack[i]);

				if(temp.min<=temp.max&&temp.max>=1){
					b[i].push_back(temp);
				}
			}
			sort(b[i].begin(),b[i].end(),big);
		}
//		for(i=0;i<n;i++){
//			for(j=0;j<b[i].size();j++){
//				cout<<b[i][j].min<<' '<<b[i][j].max<<"  ";
//			}
//			cout<<endl;
//		}
		int order[50]={0,};
		int ans=0;
		int min, max;
		int rem;
		while(true){
			for(i=0;i<n;i++){
				if(order[i]>=b[i].size()) break;
			}
			if(i!=n) break;
			min=b[0][order[0]].min;
			max=b[0][order[0]].max;
			rem=0;
			for(i=1;i<n;i++){
				if(b[i][order[i]].min>max){
					order[rem]++;
					break;
				}
				if(b[i][order[i]].max<min){
					order[i]++;
					if(order[i]>=b[i].size()) break;
					i--;
					continue;
				}
				else if(b[i][order[i]].min>min){
					min=b[i][order[i]].min;
				}
				else if(b[i][order[i]].max<max){
					max=b[i][order[i]].max;
					rem=i;
				}
			}
			if(i==n){
				ans++;
				for(j=0;j<n;j++){
					order[j]++;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
