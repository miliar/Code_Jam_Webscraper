#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <map>
#include <cmath>
using namespace std;
#define forn(i,n) for(int i=0;i<n;i++)
#define forn1(i,n) for(int i=1;i<=n;i++)
#define mp make_pair
#define pb push_back
typedef long long ll;
int t,n,r,o,y,g,b,v;


int main(){
	cin>>t;
	forn(i,t){
		cin>>n>>r>>o>>y>>g>>b>>v;
		pair<int,int> bb[3];
		vector<int>nums;
		bb[0]=mp(r,0);
		bb[1]=mp(y,1);
		bb[2]=mp(b,2);
		sort(bb,bb+3,std::greater<pair<int,int> >());
		bool imp=bb[0].first>(bb[1].first+bb[2].first);
		// cout<<bb[0].first<<" "<<bb[1].first<<" "<<bb[2].first<<endl<<endl;
		if(imp){
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
			continue;
		}
		int lo=bb[1].first+bb[2].first-bb[0].first;
		forn(j,bb[0].first){
			nums.push_back(bb[0].second);
			// cout<<nums.size()<<endl;
			if(lo>0){
				nums.push_back(bb[1].second);
				nums.push_back(bb[2].second);
				bb[1].first--;
				bb[2].first--;
				lo--;
			}else{
				if(bb[1].first>0){
					nums.push_back(bb[1].second);
					bb[1].first--;
				}else{
					nums.push_back(bb[2].second);
					bb[2].first--;
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		string s="";
		forn(j,nums.size()){
			if(nums[j]==0){
				s+="R";
			}else if(nums[j]==1){
				s+="Y";
			}else
				s+="B";
		}
		cout<<s<<endl;


	}
}