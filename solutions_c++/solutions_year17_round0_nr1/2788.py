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
	int n;
	freopen("d:\\temp\\al.in", "rt", stdin);
	freopen("d:\\temp\\al.out", "wt", stdout);
	cin>>n;

	for (int i = 1; i <=n; ++i){
		string s;
		int k;
		cin>>s>>k;
		int c = 0;
		for (int j = 0; j < s.length() - k + 1; ++j){
			if (s[j] != '+'){
				++c;
				for (int l = 0; l < k; ++l){
					if (s[j + l] == '-') s[j + l] = '+';
					else s[j + l] = '-';
				}
			}
		}
		bool pos = true;
		for (int j = 0; j < s.length(); ++j){
			if (s[j] == '-') pos = false;
		}
		cout<<"Case #"<<i<<": ";
		if (pos) cout<<c<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}