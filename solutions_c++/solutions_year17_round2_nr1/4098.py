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

int main()
{
	//to calculate the run time of the algo
	//time_t t=clock();
	//cout<<(double)(clock()-t)/CLOCKS_PER_SEC<<endl;
	int t;
	cin >> t;
	fl(i, 1, t + 1){
		int d, n;
		cin >> d >> n;
		vector<pair<ill, ill>> horses;
		fl(j, 0, n){
			
			int temp1, temp2;
			cin >> temp1 >> temp2;
			horses.push_back(make_pair(temp1, temp2));
		}
		sort(horses.begin(), horses.end(), pairCompare2);
		double time = 0.00;
		double loc = horses[0].first;
		ill min_speed = horses[0].second;
		fl(k, 1, n){
			if (horses[k].second < min_speed){
				double temp_time = (horses[k].first - loc) / double(min_speed - horses[k].second);
				double temp = (temp_time*min_speed + loc);
				if ( temp < d){
					time += temp_time;
					loc = temp;
					min_speed = horses[k].second;
				}
			}
		}
		time += (d - loc) / min_speed;
		time = d / time;
		cout << "Case #" << i << ": ";
		printf("%.6lf\n",time);
	}
	//system("pause");
	return 0;
}
