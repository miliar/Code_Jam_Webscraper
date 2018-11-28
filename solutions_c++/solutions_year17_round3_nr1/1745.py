#include <bits/stdc++.h>

#define PAUSE system("pause")
#define LL long long int
#define LD long double
#define PB push_back
#define PF push_front
#define MP make_pair
#define FORi(i, a, b) for(int i = a; i < b ; ++i)
#define FORd(i, a, b) for(int i = a; i > b ; --i)

using namespace std;

const double PI = 3.14159265359;

struct comp{
	bool operator()(pair<LL, LL>& l, pair<LL, LL>& r){
		return 1ll * l.first * l.second < 1ll * r.first * r.second;
	}
};

int main(int argc, char **argv)
{
	ifstream fin("/home/roman/CodeliteProjects/Competitive/GCJ17_R1C/in.txt");
	ofstream fout("/home/roman/CodeliteProjects/Competitive/GCJ17_R1C/out.txt");
	
	int t;
	fin >> t;
	FORi(testcase, 0, t){
		LL n,k,r,h;
		priority_queue<pair<LL, LL>, vector<pair<LL, LL> >, comp> pq;
		fin >> n >> k;
		FORi(i,0,n){
			fin >> r >> h;
			pq.push(MP(r,h));
		}
		
		vector<pair<LL, LL> > v(k);
		LL sum=0, maxr=0;
		FORi(i,0,k){
			r = pq.top().first;
			h = pq.top().second;
			v[i] = MP(r,h);
			sum += r*h;
			maxr = max(maxr, r);
			pq.pop();
		}
		
		LL max_sum = 2*sum + maxr*maxr;
		while(pq.size()){
			r = pq.top().first;
			h = pq.top().second;
			pq.pop();
			
			FORi(i,0,k){
				if (2*(sum-v[i].first*v[i].second+r*h) + r*r > max_sum){
					max_sum = 2*(sum-v[i].first*v[i].second+r*h) + r*r;
				}
			}
		}
		
		double ans = PI * max_sum;
		
		fout << "Case #" << testcase+1 << ": " << fixed << setprecision(8) << ans << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
