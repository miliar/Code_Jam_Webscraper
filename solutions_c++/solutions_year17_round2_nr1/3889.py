#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>

using namespace std;
//bool pairCompare(const std::pair<double, double>& firstElem, const std::pair<double, double>& secondElem) {
//	return firstElem.first < secondElem.first;
//
//}
//double calculate(vector<pair<double, double> >cc, double S){
//	double total_time = 0;
//	if (cc.size() == 1){
//		total_time = (S-cc[0].first)/cc[0].second;
//		return total_time;
//	}
//	if (cc.size() == 2){
////		if (cc[i].second > cc[i+1].second){
////			double tt = (cc[i+1].first -cc[i].first)/(cc[i].second - cc[i+1].second);
////			total_time += tt;
////			if (i+1 == cc.size()-1) {
////				double remainings = S- (cc[i+1].first + tt * cc[i+1].second);
////				total_time += remainings/cc[i+1].second;
////				return total_time;
////			}
////		}
////		if (i+1 == cc.size()-1) {
////			double tt = (S-cc[i+1].first)/cc[i+1].second;
////			total_time += tt;
//			//cout << "Finting time" << tt;
//		if (cc[0].second > cc[1].second){
//			double ct = (cc[1].first-cc[0].first)/(cc[0].second-cc[1].second);
//			total_time += ct;
//			double ss = cc[1].first + ct * cc[1].second;
//			total_time += (S-ss)/cc[1].second;
//			return total_time;
//		} else {
//			total_time = (S-cc[0].first)/cc[0].second;
//			cout << "Lasting time" << total_time;
//			return total_time;
//		}
//	}
//	return total_time;
//}
int main(int argc, char *argv[]) {
	int t;
	cin >> t;
	for(int i = 1; i <=t; i++) {
		double S, N;
		cin >> S;
		cin >> N;
		//vector<pair<double, double> >cc;
		vector<double> hours;
		for (int j = 1; j <= N; j++) {		
			double ki, vi;
			cin>> ki;
			cin>> vi;
			//cc.push_back(make_pair(ki,vi));
			double hour = (S-ki)/vi;
			hours.push_back(hour);
		}
		//sort(cc.begin(),cc.end(),pairCompare);
		sort(hours.begin(),hours.end());
		double ret = S/hours[hours.size()-1];
		//double ret = S/hours[0];
		cout << fixed<< "Case #" << i << ": " << ret << endl;
	}
}