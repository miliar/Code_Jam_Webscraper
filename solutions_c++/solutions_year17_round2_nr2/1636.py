//============================================================================
// Name        : gcj.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;


//bool ok(double speed){
//
//}
int arr[6] ;
int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	int cn = 0;
	while(t--){
		cn++;

		int n;
		scanf("%d",&n);
		for(int i=0;i<6;i++){
			scanf("%d",&arr[i]);
		}

		vector<pair<int,char> > v;
		v.push_back(make_pair(arr[0],'R'));
		v.push_back(make_pair(arr[2],'Y'));
		v.push_back(make_pair(arr[4],'B'));

		string ans = "";
		bool bad = 0;
		while(true){
			sort(v.rbegin(),v.rend());

			char c1 = v[0].second;
			char c2 = v[1].second;

			if(v[0].first == 0 && v[1].first == 0){
				break;
			}

			if(v[1].first == 0){

				if(ans == ""){
					ans+=c1;
					v[0].first--;
				}else{

					if(ans[(int)ans.size()-1] == c1){
						bad = 1;
						break;
					}else{
						ans += c1;
						v[0].first--;
					}

				}
			}else{

				if(ans == ""){
					ans += c1;
					ans += c2;
					v[0].first--;
					v[1].first--;
				}else {
					if(ans[(int)ans.size()-1] == c1){
						swap(c1,c2);
					}
					ans += c1;
					ans += c2;
					v[0].first--;
					v[1].first--;
				}
			}
		}
		if(bad) ans = "IMPOSSIBLE";
		else if(ans.size() > 0 && ans[0] == ans[ans.size()-1]){

			int pos = -1;
			for(int i=1;i<(int)ans.size() ;i++){
				if(ans[i-1] != ans[0] && ans[i] != ans[0]){
					pos = i;
				}
			}

			if(pos == -1){
				bad = 1 ;
				 ans = "IMPOSSIBLE";
			}else{
				string tmp = "";
				for(int i=1;i<ans.size();i++){
					if(i == pos){
						tmp += ans[0];
					}
					tmp += ans[i];
				}

				ans = tmp;
			}

		}
		cout<<"Case #"<<cn<<": "<<ans<<endl;
	}
	return 0;
}
