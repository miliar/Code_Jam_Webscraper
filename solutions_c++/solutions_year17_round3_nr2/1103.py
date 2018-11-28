
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;


bool compar( const pair<pair<int,int>,char> &a, const pair<pair<int,int>,char> &b){
	return ((a.first.second - a.first.first + 1440) % 1440) > ((b.first.second - b.first.first + 1440) % 1440);
}


int main(){
	int T;
	cin >> T;

	for(int tsc=0; tsc<T; tsc++){
		int ac,aj;
		cin >> ac >> aj;

		vector<pair<pair<int,int>,char> > acts;

		for(int i=0; i<ac; i++){
			int d,c;
			cin >> c >> d;
			acts.push_back(pair<pair<int,int>,char>(pair<int,int>(c,d),'c'));
		}

		for(int i=0; i<aj; i++){
			int d,c;
			cin >> c >> d;
			acts.push_back(pair<pair<int,int>,char>(pair<int,int>(c,d),'j'));
		}

		sort(acts.begin(),acts.end());

		vector<pair<pair<int,int>,char> > b;

		for(int i=1; i<acts.size(); i++){
			if(acts[i-1].second != acts[i].second){
				b.push_back(pair<pair<int,int>,char>(pair<int,int>(acts[i-1].first.second,acts[i].first.first),
							acts[i-1].second));
			}
		}
		if(acts[acts.size()-1].second != acts[0].second){
			b.push_back(pair<pair<int,int>,char>(pair<int,int>(acts[acts.size()-1].first.second,acts[0].first.first),
						acts[acts.size()-1].second));
		}

//		cout << "b:" << endl;
//		for(int i=0; i<b.size(); i++){
//			cout << b[i].first.first << " " << b[i].first.second << endl;
//		}

		vector<pair<pair<int,int>,char> > e;

		for(int i=1; i<acts.size(); i++){
			if(acts[i-1].second == acts[i].second){
				e.push_back(pair<pair<int,int>,char>(pair<int,int>(acts[i-1].first.second,acts[i].first.first),
							acts[i-1].second));
			}
		}
		if(acts[acts.size()-1].second == acts[0].second){
			e.push_back(pair<pair<int,int>,char>(pair<int,int>(acts[acts.size()-1].first.second,acts[0].first.first),
						acts[acts.size()-1].second));
		}

		int j_sum = 0;
		int c_sum = 0;
		int diff = 0;

		for(int i=0; i<acts.size(); i++){
			if(acts[i].second == 'c') c_sum += (acts[i].first.second - acts[i].first.first + 1440) % 1440;
			else j_sum += (acts[i].first.second - acts[i].first.first + 1440) % 1440;
		}

		for(int i=0; i<e.size(); i++){
			if(e[i].second == 'c') c_sum += (e[i].first.second - e[i].first.first + 1440) % 1400;
			else j_sum += (e[i].first.second - e[i].first.first + 1440) % 1440;
		}

		for(int i=0; i<b.size(); i++){
			diff += (b[i].first.second - b[i].first.first + 1440) % 1440;
		}
//		cout << "j_sum = " << j_sum <<endl;
//		cout << "c_sum = " << c_sum <<endl;

		if(c_sum == 720 && j_sum == 720){
			cout << "Case #"<<tsc+1<<": "<<b.size()<< endl;
			continue;
		}

		if(c_sum < 720 && c_sum + diff >= 720){
			cout << "Case #"<<tsc+1<<": "<<b.size()<< endl;
			continue;
		}
		if(j_sum < 720 && j_sum + diff >= 720){
			cout << "Case #"<<tsc+1<<": "<<b.size()<< endl;
			continue;
		}


		sort(e.begin(),e.end(),compar);

		char use;
		if(c_sum < j_sum){
			use = 'c';
		}else{
			use = 'j';
		}

		int extra_switch = 0;
		int add = diff;
		for(int i=0; i<e.size(); i++){
			if(e[i].second != use){
				add += (e[i].first.second - e[i].first.first + 1440) % 1440;
				extra_switch++;
			}
			if(use == 'c' && add + c_sum >= 720) break;
			if(use == 'j' && add + j_sum >= 720) break;
		}

		cout << "Case #" << tsc+1 << ": " << b.size() + 2*extra_switch << endl;
	}
}

