#include <iostream>
#include <stdio.h>
#include <vector>

#include <string.h>
#include <algorithm>

using namespace std;

int main(){

	int T; cin >> T;
	for(int tc = 1; tc <= T; tc++){
		string ans;
		int N, R, O, Y, G, B, V; cin >> N >> R >> O >> Y >> G >> B >> V;
		if(O > 0 && B < O+1){
			ans = "IMPOSSIBLE";
		}else if(O > 0) B -= (O+1);
		if(G > 0 && R < G+1){
			ans = "IMPOSSIBLE";
		}else if (G > 0) R -= (G+1);

		if(V > 0 && Y < V +1){
			ans = "IMPOSSIBLE";
		}else if(V > 0) Y -= (V+1);

		
		if(ans == "IMPOSSIBLE"){
			cout << "Case #"<< tc << ": " << ans << endl; continue;
		}

		int min1 = min(R, min(B, Y));
		int max1 = max(R, max(B, Y));
		int min2 = R + B + Y - min1 - max1;

		ans = "";
		if(O > 0){
			ans += "B";
			for(int i = 0; i < O; i++){
				ans += "OB";
			}
		}
		ans = "";
		if(G > 0){
			ans += "R";
			for(int i = 0; i < O; i++){
				ans += "GR";
			}
		}

		ans = "";
		if(V > 0){
			ans += "Y";
			for(int i = 0; i < O; i++){
				ans += "VY";
			}
		}
		
		vector<pair<int, string> > vec;
		vec.push_back(make_pair(R, "R"));
		vec.push_back(make_pair(B, "B"));
		vec.push_back(make_pair(Y, "Y"));

		sort(vec.begin(), vec.end());
		string s = "";

		if(vec[0].first == 0){

			
			for(int i = 0; i < vec[1].first; i++){
				s += vec[1].second;
				s += vec[2].second;
			}

			if(s.size() != R+B+Y){
				cout << "Case #"<< tc << ": " << "IMPOSSIBLE" << endl; continue;
			}
			else{
				cout << "Case #"<< tc << ": " << s << endl; continue;
			}
		}


		while(vec[1].first != vec[2].first){
			vec[0].first --;
			vec[2].first --;
			if(vec[0].first >= 0)
				s += vec[0].second;
			else break;
			if(vec[2].first >= 0)
				s += vec[2].second;
		}

		while(vec[0].first-- > 0){
			s += vec[0].second;
			s += vec[1].second;
			s += vec[2].second;
			vec[1].first--;
			vec[2].first--;
		}

		while(vec[2].first-- > 0){
			s += vec[1].second;
			s += vec[2].second;
		}

		if(s.size() != R+B+Y){
			cout << "Case #"<< tc << ": " << "IMPOSSIBLE" << endl; continue;
		}else{
			cout << "Case #"<< tc << ": " << s << endl; continue;
		}

		

	}
	return 0;
}