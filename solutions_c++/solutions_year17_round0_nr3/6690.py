#include <bits/stdc++.h>

using namespace std;

int ns;

bool check(string s) {
	for(int i = 0; i < ns-1; ++i) {
		if(s[i] > s[i+1]) {
			return false;
		}
	}
	return true;
}

bool allonezero(string s) {
	for(int i = 0; i < ns; ++i) {
		if(s[i] != '0' && s[i] != '1') {
			return false;
		}
	}
	return true;
}

int main(void) {

	ios_base::sync_with_stdio(false);

	ifstream fin;
	fin.open("C-small-1-attempt1.in");

	ofstream fout;
	fout.open("outputtt.out");

	int t;
	fin>>t;
	for(int tt = 1; tt <= t; ++tt) {
		int n, k;
		fin>>n>>k;
		int l[1001], r[1001], done[1001];
		memset(l, 0, sizeof(l));
		memset(r, 0, sizeof(r));
		memset(done, 0, sizeof(done));

		int ls, rs;
		int ind = -1;
		for(int i = 0; i < k; ++i) {
			int now = 0;
			for(int j = 0; j < n; ++j) {
				if(done[j])	{
					now = 0;
					continue;
				}
				l[j] = now;
				//if(tt == 5)	fout<<j<<" "<<l[j]<<endl;
				now++;
			}
			now = 0;
			for(int j = n-1; j >= 0; --j) {
				if(done[j])	{
					now = 0;
					continue;
				}
				r[j] = now;
				//if(tt == 5)	fout<<j<<" "<<r[j]<<endl;
				now++;
			}
			int currmax = -1;
			bool twos = false;
			ind = -1;

			for(int j = 0; j < n; ++j) {
				if(done[j])	continue;
				int m = min(l[j], r[j]);
				if(m >= currmax) {
					if(m == currmax) {
						twos = true;
						continue;
					}
					twos = false;
					currmax = m;
					ind = j;
				}
			}
			int prevmax = currmax;
			if(twos == false) {
				done[ind] = 1;
				continue;
			}

			currmax = -1;
			twos = false;
			ind = -1;
			for(int j = 0; j < n; ++j) {
				if(done[j])	continue;
				int m = max(l[j], r[j]);
				if(min(l[j], r[j]) != prevmax)	continue;
				if(m >= currmax) {
					if(m == currmax) {
						twos = true;
						continue;
					}
					twos = false;
					currmax = m;
					ind = j;
				}
			}

			int prevmax2 = currmax;
			if(twos == false) {
				done[ind] = 1;
				continue;
			}
			
			for(int j = 0; j < n; ++j) {
				if(done[j])	continue;
				if((min(l[j], r[j])) == prevmax && (max(l[j], r[j]) == prevmax2)) {
					done[j] = 1;
					ind = j;
					//fout<<"doing "<<l[i]<<" "<<r[i]<<endl;
					break;
				}
			}
		}
		//if(tt == 5)	fout<<"ind:: "<<ind<<endl;
		int minn = 100000, maxx = -1;
		int nnow = 0;
		for(int i = ind-1; i >= 0; --i) {
			if(done[i])	break;
			nnow++;
		}
		int ll = nnow;
		nnow = 0;
		for(int i = ind+1; i < n; ++i) {
			if(done[i])	break;
			nnow++;
		}
		int rr = nnow;

		fout<<"Case #"<<tt<<": ";
		fout<<max(ll, rr)<<" "<<min(ll, rr);
		fout<<"\n";

	}

	return 0;

}