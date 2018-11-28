#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <numeric>
#include <queue>
#include <map> 
#include <set>
#include <string>
#include <functional>
using namespace std;
const int INF = 1e+8;

bool check(long long num){
	std::string s;
	s = std::to_string(num);
	int mae = -1;
	for (size_t i=0; i < s.size(); i++){
		if (s[i] < mae) return false;
		mae = s[i];
	}
	return true;
}
class Node{
public:
	long long nowNum;
	long long placeNum;
	int depth;
	Node(long long now, long long place, long long dep){
		nowNum = now;
		placeNum = place;
		depth = dep;
	}
};


int main(){
	
	int caseNum;
	long long N, K;	//N:•”‰® K:l 
	cin >> caseNum;
	for (int i = 0; i < caseNum; i++){
		cin >> N >> K;
		Node n(N, 1, 0);
		vector<map<long long,long long>> binTree;
		map<long long, long long> ma;
		ma.insert(map<long long, long long>::value_type(N, 1LL));
		binTree.push_back(ma);
		//for (int j = 0; j < 60; j++){
			map<long long, long long> m;
			for (size_t k=0; k < 60; k++){
				auto it = binTree[k].begin();
				while (it != binTree[k].end()){
					long long key, value;
					key = (*it).first;
					value = (*it).second;
					if (key % 2 == 1){
						//key(ŠJ‚¢‚Ä‚¢‚éÈ‚Ì’·‚³)‚ªŠï”‚È‚çA“¯‚¶”“ñ‚Â‚É•ª‚©‚ê‚é‚Í‚¸
						if (m.count(key / 2) == 0){
							//m.insert(key / 2, value * 2);
							m.insert(map<long long, long long>::value_type(key / 2, value * 2));
						}
						else{
							m[key / 2] += value * 2;
						}
					}
					else{
						if (m.count(key / 2) == 0){
							//m.insert(key / 2, value);
							m.insert(map<long long, long long>::value_type(key / 2, value));
						}
						else{
							m[key / 2] += value;
						}
						if (m.count((key - 1) / 2) == 0){
							//m.insert((key - 1) / 2, value);
							m.insert(map<long long, long long>::value_type((key-1)/2, value));
						}
						else{
							m[(key - 1) / 2] += value;
						}

					}
					it++;
				}
				binTree.push_back(m);
				m.clear();
			}


		//}
			vector<pair<long long, long long>> answers;
		for (size_t l = 0; l < binTree.size(); l++){
			auto it = binTree[l].begin();
			while (it != binTree[l].end()){
				long long key = (*it).first, value = (*it).second;
				//cout << key << " : " << value << "\n";
				answers.push_back(make_pair(key, value));
				it++;
			}
			//cout << "===============================================\n";
		}
		sort(answers.begin(), answers.end());
		reverse(answers.begin(), answers.end());
		for (pair<long long, long long> p : answers){
			K -= p.second;
			if (K <= 0){
				cout << "Case #" << i + 1 << ": " << p.first / 2 << " " << (p.first - 1) / 2 << "\n";
				break;
			}
		}
		//cout << "Case #" << i + 1 << ": " << ans2 << " " << ans1 << "\n";
	}

	return 0;
}