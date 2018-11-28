#include <bits/stdc++.h>
#include <math.h>
using namespace std;

int main(){
    int test,s,k;
    int c[2];
    cin>>test;
	for(int tt=1;tt<=test;tt++){
		vector<pair<pair<int,int>,int>> okr;
		vector<int> prze[2];
		int t[2];
		t[0]=t[1]=0;
		cin>>c[0]>>c[1];
		for(int i=0;i<2;i++)
		for(int j=0;j<c[i];j++){
			cin>>s>>k;
			okr.emplace_back(make_pair(s,k),i);
			t[i]+=k-s;
		}
		int wyn=0;
		sort(okr.begin(),okr.end());
		okr.emplace_back(make_pair(okr[0].first.first+1440,okr[0].first.second),okr[0].second);
		for(int i=0;i<okr.size()-1;i++){
			if(okr[i].second==okr[i+1].second){
				prze[okr[i].second].emplace_back(okr[i+1].first.first-okr[i].first.second);
			}else{
				wyn++;
			}
		}
		for(int i=0;i<2;i++){
			sort(prze[i].begin(),prze[i].end());
			for(int j=0;j<prze[i].size();j++){
				if(t[i]+prze[i][j]<=720)
					t[i]+=prze[i][j];
				else
					wyn+=2;
			}
		}
		cout<<"Case #"<<tt<<": "<<wyn<<endl;
	}
	
    
    
    return 0;
}

