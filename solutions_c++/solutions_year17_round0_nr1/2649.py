#include<bits/stdc++.h>
using namespace std;

string str;
vector<bool> pan;
int K;

void flip(int index){
	for(int i = 0; i<K && (i+index)<pan.size(); i++)
		pan[index+i] = !pan[index+i];
}

int main(){
	int N; cin >> N;
	for(int cas = 1; cas<=N; cas++){
		pan.clear();
		cin >> str; cin >> K;
		for(int i = 0; i<str.size(); i++){
			if (str[i] == '-') pan.push_back(false);
			else pan.push_back(true);
		}
		//for(int i = 0; i<pan.size(); i++) cout << pan[i];
		//cout << " " << K << endl;

		int count = 0;
		bool pos = true;
		for(int i = 0; i<pan.size(); i++){
			if (pan[i] == false && (pan.size() - i) >= K) {
				count++;
				flip(i);
			}
			if (pan[i] == false && (pan.size() - i) < K) {
				cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
				pos = false;
				break;
			}
		}
		if (pos)	
			cout << "Case #" << cas << ": " << count << endl;

	}
}
