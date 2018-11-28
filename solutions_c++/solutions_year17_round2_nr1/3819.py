#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// functions go here
double speed(double d, vector<vector<double> > v)
{
	vector<vector<double> > vResult = v;
	vector<double> vTime(v.size());
	vector<vector<double> > vv(v.size(),vector<double>(2,0) );
	vResult[0][0] = d - v[0][0];
	for (int i = 1; i < vResult.size(); i++ )
	{
		vResult[i][0] = v[i - 1][0] - v[i][0];
	}

	// cout << vResult[0][0] << " " << vResult[0][1] << endl;
	// cout << vResult[1][0] << " " << vResult[1][1] << endl;

	double td, tcatch, result;
	double sum = 0;
	for (int j = 0; j < vResult.size(); j++)
	{
		td = (d - v[j][0])/v[j][1];
		tcatch = vResult[j][0]/v[j][1];

		vTime[j] = td;
		vv[j][0] = td;
		vv[j][1] = j;
		//vTime[j][1] = tcatch;
	}

	sort(vTime.begin(), vTime.end());
	sort(vv.begin(), vv.end());
	// for (int k = 1; k < vTime.size(); k++)
	// {
	// 	if (vTime[k][1] < vTime[k - 1][0])
	// 	{
	// 		vTime[k][0] = vTime[k - 1][0];
	// 	}
	// }
	result = d/vTime[vTime.size() - 1];
	//int index = vv[vv.size() - 1][1];
	// = result < v[index][1] ? result : v[index][1];
	// for (int k = v.size() - 1; k >= 0; k--)
	// {
	// }

	return result;
}


// main function
int main() 
{
	int t, d, n;
  	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  	for (int i = 1; i <= t; ++i) {
    cin >> d >> n;  // read n and then m.
    std::vector<std::vector<double> > v;
    for (int j = 0; j < n; j++) {
    	v.push_back(std::vector<double> (2, 0));
    	cin >> v[j][0] >> v[j][1];
    }
    double answer = speed(d, v);
    cout << fixed << "Case #" << i << ": " << answer << endl;
  }

  return 0;
}