#include <bits/stdc++.h>

using namespace std;

string solve(int blue, int yellow, int red){
	vector<pair<int, string> > save;
	
	save.push_back(make_pair(blue, "B"));	
	save.push_back(make_pair(red, "R"));
	save.push_back(make_pair(yellow, "Y"));

	sort(save.begin(), save.end());

	reverse(save.begin(), save.end());

	string ans;

	for(int i = 0 ; i<save[0].first ;i++)	{
		ans+=save[0].second;
	}
	char letter = save[1].second[0];
	int ind = 0;

	for(int i = 0 ; i<save[1].first ; i++){
		int ind1 = ind;
		int ind2 = ind+1;

		if(ind1+1 == ans.size()){
			ind2 = 0;
		}	

		if(ans[ind1]!=letter && ans[ind2]!=letter){
			string tmp = "";
			tmp+=letter;
			ans.insert(ind1 +1,tmp);
			ind+=2;	
		}
		if(ind2 == 0){
			ind = 0;	
		}
	}	

	letter = save[2].second[0];

	for(int i = 0 ; i<save[2].first ; i++){
		int ind1 = ind;
		int ind2 = ind+1;
		
		if(ind1+1 == ans.size()){
			ind2 = 0;
		}	

		if(ans[ind1]!=letter && ans[ind2]!=letter){
			string tmp = "";
			tmp+=letter;
			ans.insert(ind1 +1, tmp);
			ind+=2;	
		}
		if(ind2 == 0){
			ind = 0;	
		}
	}	

	if(ans[0] == ans[ans.size()-1]){
		return "IMPOSSIBLE";	
	}
	return ans;

}

int main(){
	int TC,NC = 1;

	cin>>TC;

	while(TC--){
	
		int n, red, orange, yellow, green, blue, violet;

		cin>>n;

		cin>>red>>orange>>yellow>>green>>blue>>violet;

		string ans = solve(blue, yellow, red);
	
		cout<<"Case #"<<NC++<<": "<<ans<<endl;
	
		
	}

	return 0;	
}
