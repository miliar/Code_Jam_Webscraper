#include <iostream>
#include <string>

using namespace std;

int main()
{
	int total;
	cin>>total;
	for (int p = 0; p < total; ++p) {
		string s;
		cin>>s;
		int k;
		cin>>k;
		int size = s.size()-k+1;
		int tmp[size];
		if (s[0] == '-') tmp[0] = 1;
		else tmp[0] = 0;
		int pre = tmp[0];
		int res = tmp[0];
		for (int i = 1; i < size; ++i) {
			if (i - k >= 0) {
				pre ^= tmp[i-k];
			} 
			int cur;
			if (s[i] == '-') cur = 1;
			else cur = 0;
			if (0 ^ pre == cur) tmp[i] = 0;
			else {
				tmp[i] = 1;
				++res;
			}
			pre ^= tmp[i];
		}
		// for (int i = 0; i < size; ++i) {
		// 	cout<<tmp[i]<<" ";
		// }
		// cout<<endl;
		bool exist = true;
		for (int i = size; i < s.size(); ++i) {
			if (size - k >= 0) pre ^= tmp[size-k];
			--k;
			if (s[i] == '-' && pre == 0 || s[i] == '+' && pre == 1) {
				exist = false;
				break;
			}
		}
		if (exist) cout<<"Case #"<<p+1<<": "<<res<<endl;
		else cout<<"Case #"<<p+1<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}