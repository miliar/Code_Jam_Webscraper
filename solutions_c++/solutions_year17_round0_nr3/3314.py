#include <vector>
#include <iostream>
#include <string>
#include <functional>
#include <algorithm>

using namespace std;

int main(){
	long long t;
	vector<string> ans;
	cin >> t;
	for (long long i = 0; i < t; i++)
	{
		string this_ans;
		long long n, k, a = 1, b = 1, s;
		cin >> n >> k;
		while (2 * a <= n)
			a *= 2;
		while (b <= k)
			b *= 2;
		s = (2*(a / b - 1) + (n - a + 1) / (b / 2));
		if ((n - a + 1) % (b/2) >= (k - b/2 + 1))
			s++;
		if (s % 2 == 1)
			this_ans = to_string(s / 2 + 1) + " ";
		else
			this_ans = to_string(s / 2) + " ";			
		this_ans = this_ans + to_string(s/2);
		ans.push_back(this_ans);
	}
	for (long long i = 0; i < ans.size(); i++)
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	
	return 0;
}