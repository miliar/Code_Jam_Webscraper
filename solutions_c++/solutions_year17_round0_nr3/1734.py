#include <iostream>
#include <cmath>
#include <map>
#include <functional>

using namespace std;

int main()
{
	int test = 0;
	long N = 0, k = 0, minVal = 0, maxVal = 0;
	map<long, long, greater<long> > values;
	cin >> test;
	for (int t = 0; t < test; ++t){
		cin >> N >> k;
		values[N] = 1;
		for (;k > 0;){
//for (auto& x: values)
//cout << x.first << "-" << x.second << endl;
//cout << "k=" << k << endl;
			auto tmp = values.begin();
			long val = tmp->first;
			long count = tmp->second;
			values.erase(tmp);
			minVal = (val - 1)/2;
			maxVal = val - minVal - 1;
			if (values.find(minVal) == values.end())
				values[minVal] = count;
			else
				values[minVal] += count;
			if (values.find(maxVal) == values.end())
				values[maxVal] = count;
			else
				values[maxVal] += count;
			k -= count;	
		}
		cout << "Case #" << t+1 << ": ";
		cout << maxVal << " " <<  minVal;
		cout << endl;
		values.clear();
	}

	return 0;
}
