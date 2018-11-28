#include<iostream>
#include<vector>
using namespace std;


struct Ticket {
	int p, b;
};




int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		int n, m, c;
		cin >> n >> c >> m;
		
		vector<Ticket> ticket(m);
		vector<int> cntByCustomer(c, 0), cntBySeat(n, 0);
		
		for(int i=0;i<m;i++) {
			int p, b;
			cin >> p >> b;
			p--, b--;
			
			cntByCustomer[b]++;
			cntBySeat[p]++;
		}
		
		int result = 0;
		for(int i=0;i<c;i++)
			result = max(result, cntByCustomer[i]);
			
		{
			int sum = 0;
			for(int i=0;i<n;i++) {
				sum += cntBySeat[i];
				result = max(result, (sum+i) / (i+1));
			}
		}
		
		int promo = 0;
		for(int i=0;i<n;i++)
			promo += max(0, cntBySeat[i] - result);
		
		cout << "Case #" << TCASE << ": " << result << ' ' << promo << '\n';
	}
	
	return 0;
}

