#include <bits/stdc++.h>

using namespace std;


int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		char color[] = {'R', 'O', 'Y', 'G', 'B', 'V'};
		cout << "Case #" << t << ": ";
		pair<int, char>  horses[6];
		int N;
		cin >> N;
		int zeros = 0;
		for(int i=0; i<6; i++){
			int k;
			cin >> k;
			if(k == 0) zeros ++;
			horses[i] = make_pair(k, color[i]);
		}

		if(zeros == 4){
			if(horses[0].first > 0 && horses[3].first == horses[0].first){
				for(int i=0; i<N/2; i++){
					cout << "RG";
				}
				cout << endl;
				continue;
			} else if(horses[1].first > 0 && horses[1].first == horses[4].first){
				for(int i=0; i<N/2; i++){
					cout << "OB";
				}
				cout << endl;
				continue;
			} else if(horses[2].first > 0 && horses[2].first == horses[5].first){
				for(int i=0; i<N/2; i++){
					cout << "YV";
				}
				cout << endl;
				continue;
			}
		}

		if((horses[0].first <= horses[3].first && horses[3].first != 0) || (horses[2].first <= horses[5].first && horses[5].first != 0) || (horses[4].first <= horses[1].first && horses[1].first != 0)){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}


		int orange = horses[1].first, green = horses[3].first, violet = horses[5].first;
		horses[1].first = horses[3].first = horses[5].first = 0;
		horses[0].first -= green;
		horses[2].first -= violet;
		horses[4].first -= orange;

		swap(horses[1], horses[4]);
		sort(horses, horses + 3);
		reverse(horses, horses + 3);


		if(horses[0].first > (horses[1].first + horses[2].first)){
			cout << "IMPOSSIBLE" << endl;
		} else {
			int NN = horses[0].first + horses[1].first + horses[2].first;
			string res = "";
			res += horses[0].second;
			horses[0].first --;
			for(int i=1; i<NN; i++){
				if(res[i-1] == horses[0].second){
					if(horses[1].first > horses[2].first || (horses[1].first == horses[2].first && res[0] == horses[1].second)){
						res += horses[1].second;
						horses[1].first --;
					} else {
						res += horses[2].second;
						horses[2].first--;
					}
				} else if(res[i-1] == horses[1].second){
					if(horses[0].first > horses[2].first || (horses[0].first == horses[2].first && res[0] == horses[0].second)){
						res += horses[0].second;
						horses[0].first --;
					} else {
						res += horses[2].second;
						horses[2].first--;
					}
				} else {
					if(horses[1].first > horses[0].first || (horses[1].first == horses[0].first && res[0] == horses[1].second)){
						res += horses[1].second;
						horses[1].first --;
					} else {
						res += horses[0].second;
						horses[0].first--;
					}
				}
			}
			if(green != 0){
				for(int i=0; i<res.size(); i++){
					if(res[i] == 'R'){
						string news = "R";
						string before = res.substr(0, i);
						string after = "";
						if(i != res.size()-1)
							after = res.substr(i+1, res.size() - 1 - i);
						for(int j=0; j<green; j++){
							news += "GR";
						}
						res = before + news + after;
						break;
					}
				}
			}

			if(orange != 0){
				for(int i=0; i<res.size(); i++){
					if(res[i] == 'B'){
						string news = "B";
						string before = res.substr(0, i);
						string after = "";
						if(i != res.size()-1)
							after = res.substr(i+1, res.size() - 1 - i);
						for(int j=0; j<orange; j++){
							news += "OB";
						}
						res = before + news + after;
						break;
					}
				}
			}
			if(violet != 0){
				for(int i=0; i<res.size(); i++){
					if(res[i] == 'Y'){
						string news = "Y";
						string before = res.substr(0, i);
						string after = "";
						if(i != res.size()-1)
							after = res.substr(i+1, res.size() - 1 - i);
						for(int j=0; j<violet; j++){
							news += "VY";
						}
						res = before + news + after;
						break;
					}
				}
			}
			cout << res << endl;
		}
	}

	return 0;
}


