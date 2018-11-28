#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

int tidy(string& num, int index){
	if(index < 1)
		return num.length()+10;
	bool sw = false;
	if(num[index] < num[index-1]){
		num[index-1] = char(num[index-1]-1);
		sw = true;
	}

	int minIndex = tidy(num, index-1);
	if(sw)
		return min(minIndex, index);
	return minIndex;
}

int main(){
	int t, count = 1;
	cin >> t;
	while(count <= t){
		//cout << "--------------" << endl;

		string num;
		cin >> num;
		//cout << "num " << num;

		int i = tidy(num, num.length()-1);
		//int minIndex = i;
		for(; i < num.length(); ++i)
			num[i] = '9';

		//cout << " minIndex : " << minIndex << " str: " << num << endl;

		cout << "Case #" << count << ": ";
		bool leadingzeroes = true;
		for(int j = 0; j < num.size(); ++j){
			if(num[j] == '0' && leadingzeroes)
				continue;
			leadingzeroes = false;
			cout << num[j];
		}
		cout << endl;
		count++;
	}
}