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
#include <string>
#include <algorithm>
using namespace std;

void main(){
	int t;
	freopen("d:\\temp\\bl.in", "rt", stdin);
	freopen("d:\\temp\\bl.out", "wt", stdout);
	cin>>t;

	for (int o1 = 1; o1 <=t; ++o1){
		string s;
		cin>>s;
		int c = 0;
		for (int j =  s.length() - 2; j >= 0; --j){
			if (s[j] > s[j + 1]){
				--s[j];
				int k = j + 1;
				while (k < s.length() && s[k] != '9'){
					s[k] = '9';
					++k;
				}
			}
		}
		
		long long mul = 1;
		long long n = 0;
		for (int j =  s.length() - 1; j >= 0; --j){
			n += mul * (s[j] - '0');
			mul *= 10;
		}
		cout<<"Case #"<<o1<<": "<<n <<endl;
	}
}