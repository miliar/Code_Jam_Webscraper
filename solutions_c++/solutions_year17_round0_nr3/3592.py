#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
#include <climits>
#include <queue>
#include <numeric>
#include <thread>
using namespace std;

int calc(int64_t N,int64_t K)
{
	int64_t M = K;
	int l = 0;
	while (K)
	{
		K >>= 1;
		l++;
	}
	int64_t stalledPeopleLastlayer = pow(2, l - 1)-1;
	int64_t newPeople = M - stalledPeopleLastlayer;
	N -= stalledPeopleLastlayer;
	int64_t remainder = N%(stalledPeopleLastlayer+1);
	int64_t ans = N / (stalledPeopleLastlayer+1);
	if (remainder >= newPeople)
		return ans + 1;
	else
		return ans;
}
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	int64_t T, N,res,K;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cin >> N>>K;
		res = calc(N, K);
		if (res%2)
			cout << "Case #" << t << ": " << res / 2 <<" "<< res / 2 << endl;
		else
			cout << "Case #" << t << ": " << (res+1) / 2 << " " << (res-1) / 2 << endl;
	}

	return 0;
}
