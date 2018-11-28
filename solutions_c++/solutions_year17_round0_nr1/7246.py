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

bool check(string s){
	fl(i, 0, s.length()){
		if (s[i] == '-'){
			return false;
		}
	}
	return true;
}
int main()
{
	//to calculate the run time of the algo
	//time_t t=clock();
	//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
	int t;
	cin >> t;
	fl(test, 1, t + 1){
		string s;
		int k;
		cin >> s >> k;
		int result = 0;
		fl(i, 0, s.length() - k + 1){
			while (s[i] == '+' && i<s.length())
			{
				++i;
			}
			if ((i < s.length() && i > s.length() - k) || i == s.length())
			{
				break;
			}
			fl (j,i,i+k){
				if (s[j] == '+'){
					s[j] = '-';
				}
				else{
					s[j] = '+';
				}
			}
			++result;
		}
		if (!check(s)){
			cout << "Case #" << test << ": " << "IMPOSSIBLE"<<"\n";
		}
		else{
			cout << "Case #" << test << ": " << result << "\n";
		}
	}
	//system("pause");
	return 0;
}
