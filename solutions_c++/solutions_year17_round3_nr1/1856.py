#include <bits/stdc++.h>
using namespace std;
#define lln long long int

int main(){
	lln t;
	cin >> t;
	for(lln i=0;i<t;i++){
		lln n,k;
		cin >> n >> k;
		lln r[n];
		vector <pair <lln,lln> > h;
		map <lln,lln> mp;
		for(lln j=0;j<n;j++){
			lln x,y;
			cin >> x >> y;
			r[j] = x*x;
			h.push_back(make_pair(2*x*y,j));
			mp.insert(make_pair(j,2*x*y));
		}
		sort(h.rbegin(),h.rend());
		lln ans = INT_MIN;
		for(lln j=0;j<n;j++){
			lln sum = 0;
			sum = sum + r[j] + mp[j];//cout << r[j] << " " << mp[j] << endl;
			lln u = 1;
			lln poi = 0;
			while(u<k){
				if(h[poi].second!=j){
					sum += h[poi].first;//cout << h[poi].first << endl;
					u++;
				}
				poi++;
			}
			if(sum > ans)
				ans = sum;
		}
		double sol = (double)(ans * 3.141592653589793238462643383279502884197169399);
		cout << "Case #" << i+1 << ": ";
		printf("%0.9f\n",sol);
	}
	return 0;
}