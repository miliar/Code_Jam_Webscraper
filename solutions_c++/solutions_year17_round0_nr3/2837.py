//#include <iostream>
//#include <algorithm>
//#include <vector>
//using namespace std;
//
//int n, m;
//vector<int> usedn;
//vector<int> usedm;
//
//long long solve(vector<vector<int>> mas)
//{
//
//}
//
//void main(){
//	cin>>n>>m;
//	vector<vector<int>> inp(n, vector<int>(m));
//	vector<vector<int>> mas1(n, vector<int>(m));
//	vector<vector<int>> mas2(m, vector<int>(n));
//	usedn.assign(n, 0);
//	usedm.assign(m,0);
//	for (int i = 0; i < n; ++i)
//		for (int j = 0; j < m; ++j)
//	{
//		cin>>mas1[i][j];
//		inp[i][j] = mas1[i][j];
//		mas2[j][i] = mas1[i][j];
//	}
//	for (int i = 0; i < n; ++i)
//	{
//		sort(mas1[i].begin(), mas1[i].end());
//	}
//	for (int j = 0; j < m; ++j)
//		{
//		}
//
//}
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void main(){
	int t;
	freopen("d:\\temp\\c3.in", "rt", stdin);
	freopen("d:\\temp\\c3.out", "wt", stdout);
	cin>>t;

	for (int o1 = 1; o1 <=t; ++o1){
		long long n, k;
		cin>>n>>k;
		map<long long, long long> dists;
		dists.insert(pair<long long, long long>(n, 1));
		auto it = dists.rbegin();
		while (k > it->second){
			k -= it->second;
			dists[it->first / 2] += it->second;
			dists[(it->first - 1) / 2] += it->second;
			++it;
		}
		cout<<"Case #"<<o1<<": "<<it->first / 2<<" "<< (it->first - 1) / 2<<endl;
	}
}