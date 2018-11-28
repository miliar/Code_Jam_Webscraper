#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 0; TCASE < T; TCASE++) {
		cout << "Case #" << TCASE+1 << ": ";
		string n;
		cin >> n;
		vector<long long> tpow(n.size(), 1);
		for(int i=int(n.size())-2; i >= 0; i--)
			tpow[i] = tpow[i+1]*10;
		
		long long result = 0;
		
		{
			bool valid = true;
			for(int i=0;i+1<(int)n.size();i++)
				if(n[i] > n[i+1])
					valid = false;
			
			if(valid)
				for(int i=0;i<(int)n.size();i++)
					result += tpow[i] * (n[i]-'0');
		}
		
		for(int mid = 0; mid < int(n.size());mid++) if(n[mid] > '0') {
			long long ret = tpow[mid] * (n[mid]-'1');
			
			for(int i=mid+1;i<int(n.size()); i++)
				ret += tpow[i] * 9;
			
			int dig = n[mid]-'0';
			
			for(int i=mid-1;i >=0 ;i--) {
				dig = min(dig, int(n[i]-'0'));
				ret += tpow[i] * dig;
			}
			
			result = max(result, ret);
		}
		
		cout << result << '\n';
	}
	return 0;
}

