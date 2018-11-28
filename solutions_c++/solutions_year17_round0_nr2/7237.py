//Author : Aman Sinha
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <cstring>
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
#include <climits>
#include <queue>
#include <iterator>
using namespace std;
typedef long long int ill;
#define fl(i,START,END) for(ill i=START;i<END;++i)
#define rfl(i,START,END) for(ill i=START;i>END;--i)

bool pairCompare1(const std::pair<string, int>& firstElem, const std::pair<string, int>& secondElem) {
	return firstElem.second > secondElem.second;
}

bool pairCompare2(const std::pair<int, int>& firstElem, const std::pair<int, int>& secondElem) {
	return firstElem.first < secondElem.first;
}

void init(int arr[], int size, int val)
{
	fl(i, 0, size)
	{
		arr[i] = val;
	}
}

bool isTidy(string s, int& index){
	fl(i, 0, s.length()-1){
		if (s[i] > s[i + 1]){
			index = i;
			return false;
		}
	}
	return true;
}

void fill(string& s){
	string t = "";
	fl(i, 0, s.length()){
		if (s[i] == '0')
		{
			s[i] = '9';
		}
	}
	return;
}
string getTidy(string s){
	int index = -1;
	if (isTidy(s,index)){
		return s;
	}
	else{
		int length = s.length();
		fl(i, index + 1, length){
			s[i] = '9';
		}
		s[index]--;
		rfl(i, index-1, -1){
			if (s[i] <= s[i + 1]){
				break;
			}
			s[i]--;
			s[i + 1] = '9';
		}
		if ((s[0] > s[1]) || (s[0] <='0')){
			s.erase(s.begin() + 0);
		}
	}
	fill(s);
	return s;
}

int main()
{
	//to calculate the run time of the algo
	//time_t t=clock();
	//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
	int t;
	cin >> t;
	fl(i,1,t+1){
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << getTidy(s)<<"\n";
	}
	return 0;
}
