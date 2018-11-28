#include <bits/stdc++.h>
using namespace std;
int main(){
	int t,k,n;
	std::vector<pair<int,int> > ans;
	cin>>t;
	while(t--){
		cin>>n>>k;
		std::vector<pair<int,int> > ve1;
		std::vector<int> ve2;
		ve1.push_back(make_pair(1,n));
		ve2.push_back(n-1+1);		
		for (int i = 0; i < k; ++i){
			int Max=-1,pos=0,izq=INT_MAX,der=0,sum=0;
			for (int j = 0; j < ve2.size(); ++j){
				if(ve2[j]>=Max){
					if(ve2[j]==Max){
						if(ve1[j].first<izq){
							izq=ve1[j].first;
							pos=j;
						}
					}
					else{	
						Max=ve2[j];
						izq=ve1[j].first;
						pos=j;
					}
				}
			}
			for (int j = ve1[pos].first; j <= ve1[pos].second; ++j){
				sum+=j;
			}
			sum/=ve2[pos];
			//cout<<sum<<"fasdf"<<endl;
			if(sum-1>=ve1[pos].first){
				ve1.push_back(make_pair(ve1[pos].first,sum-1));
				ve2.push_back((sum-1)-ve1[pos].first+1);
			}
			else{
				ve2.push_back(0);
				ve1.push_back(make_pair(0,0));
			}
			if(sum+1<=ve1[pos].second){
				ve1.push_back(make_pair(sum+1,ve1[pos].second));
				ve2.push_back(ve1[pos].second-(sum+1)+1);
			}
			else{
				ve2.push_back(0);
				ve1.push_back(make_pair(0,0));
			}
			ve2[pos]=-9;
			int r1=ve2[ve2.size()-1];
			int r2=ve2[ve2.size()-2];
			if(i==k-1){
				ans.push_back(make_pair(max(r1,r2),min(r1,r2)));
				//cout<<max(r1,r2)<<" "<<min(r1,r2)<<endl;
			}
		}
	}
	for (int i = 0; i < ans.size(); ++i){
		cout<<"Case #"<<i+1<<": "<<ans[i].first<<" "<<ans[i].second<<endl;
	}
	//system("pause");
	return 0;
}