#include<bits/stdc++.h>

using namespace std;

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	
	for(int tc = 1;tc<=t;tc++){
		int n,k;
		cin>>n>>k;
		map<int,int> mp;
		mp[n] = 1;
		cout<<"Case #"<<tc<<": ";
		int l,r;
		while(k--){
			map<int,int>::iterator it = mp.end();
			it--;
			l = (it->first)/2;
			r = (it->first)-((it->first)/2)-1;
			mp[l]++;
			mp[r]++;
			if(mp[it->first]> 1)
			mp[it->first]--;
			else 
			mp.erase(it);
			
			/*cout<<"\n---------------\n";
			for(map<int,int>::iterator it = mp.begin();it!=mp.end();++it){
				cout<<(it->first)<<" "<<(it->second)<<"\n";
			}
			cout<<"---------------\n";*/
		}
		cout<<max(l,r)<<" "<<min(l,r)<<endl;
	}
	return 0;
}
