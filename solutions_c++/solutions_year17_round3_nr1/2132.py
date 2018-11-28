#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <unordered_map>
#include <string>
#include <utility>
#include <unordered_set>
using namespace std;

double PI=3.14159265359;

double calculateSides(int height,int radius) {
	return 2*M_PI*radius*height;
}

bool orderByRadius (pair<int, int> i,pair<int, int> j) { 
	return (i.second>=j.second);
}
bool orderBySides (pair<int, int> i,pair<int, int> j) { 
	return (calculateSides(i.first,i.second)>=calculateSides(j.first,j.second));
}



int main() {
	int t;
	cin >> t;
	for (int test = 0; test < t; test++) {
		int n,k;
		cin >> n >> k;
		vector < pair <int, int> > pancakes;
		vector <int> radius;
		for (int i=0; i < n; i++) {
			int h,r;
			cin >> r >> h;
			pancakes.push_back(make_pair(h,r));
		}
		double totalSum=0.0;
		
		sort(pancakes.begin(),pancakes.end(),orderByRadius);
		for (int i=0; i <pancakes.size();i++) {
			//cout << pancakes[i].first << " " << pancakes[i].second << endl;
		}
		for (int i=0; i <= n-k; i++) {
			//cout << "checking index " << i << " " << endl; 
			double currentSum=0.0;
			currentSum+=calculateSides(pancakes[i].first,pancakes[i].second)+(M_PI*pancakes[i].second*pancakes[i].second);
			vector < pair <int, int> > tmp = pancakes;	
			tmp.erase (tmp.begin(),tmp.begin()+i+1);
			sort(tmp.begin(),tmp.end(),orderBySides);
			for (int index=0;index < tmp.size(); index++) {
				//cout << "position " << index << " has " << tmp[index].first << " " << tmp[index].second << endl; 
			}
			for (int j=0; j < k-1; j++) {
				currentSum+=calculateSides(tmp[j].first,tmp[j].second);
			}
			totalSum=max(totalSum,currentSum);
		}	
		cout.precision(9);
		cout << fixed;
		cout << "Case #" << test+1 << ": " << totalSum << endl;
	}
	return 0;
}