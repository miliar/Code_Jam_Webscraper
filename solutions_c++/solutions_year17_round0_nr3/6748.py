#include <bits/stdc++.h>
using namespace std;

int main() {
	//freopen("in.in","rt",stdin);
	//freopen("newfile.txt","wt",stdout);
	int z;
	cin >> z;
	for (int t = 1; t <= z; t++) {
		long long n, k;
		cin >> n >> k;
		long long v = k - 1;
		priority_queue<long long> q;
		q.push(n);
		while (v--) {
			long long f = q.top();
			q.pop();
			long long nx = f / 2;
			if (f == 1)
				continue;
			q.push(nx);
			q.push(f - nx - 1);
		}
		long long mx = -1e9, mn = 1e9;
		long long z = q.top(), zz = z / 2;
		//cout << z << "<<\n";
		q.pop();
		if (z == 0) mx=mn=0;

		mx = max(mx, max(zz, z - zz - 1));
		mn = min(mn, min(zz, z - zz - 1));
		/*
		 while(q.size()){
		 long long z=q.top(),zz=z/2;
		 cout<<z<<"<<\n";
		 q.pop();
		 if(z==0) break;
		 mx=max(mx,max(zz,z-zz-1));
		 mn=min(mn,min(zz,z-zz-1));
		 }*/
		cout << "Case #"<<t<<": "<<mx << " " << mn << "\n";
	}
	return 0;
}

