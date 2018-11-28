#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

#define all(a) a.begin(),a.end()

using namespace std;

struct Pank{
	int R, H;
};

bool pankCompare(Pank lhs, Pank rhs) {return lhs.R < rhs.R; };



struct Solver {
	int N, K;
	vector<Pank> panks;
	vector <int> indexes;
	double ans;
	void read() {
		cin >> N;
		cin >> K;
		panks.resize(N);
		for(int i=0; i<N; i++){
			cin >> panks[i].R;
			cin >> panks[i].H;
		}
		sort(panks.begin(), panks.end(), pankCompare);
	}

	void solve() {
		indexes.resize(K);
		ans = 0.0;
		for(int i=0; i<K; i++){
			indexes[i] = i;
		}
		while(1){
			bool end = false;
			double anst = 0;
			double r , h;
			for(int i=0; i<K; i++){
				r = panks[indexes[i]].R;
				h = panks[indexes[i]].H;
				anst += 2.0 * M_PI * r * h;
			}
			anst += M_PI * r * r;
			if(anst>ans)
				ans = anst;
			for(int i=K-1; i>=0; i--){
				bool x = false;
				indexes[i]++;
				if(indexes[i]>=N && i==0){
					end = true;
					break;
				}
				for(int j=i+1; j<K; j++){
					indexes[j] = indexes[j-1] + 1;
					if(indexes[j]>=N){
						x = true;
						if(i==0)
							end = true;
						break;
					}
				}
				if(x)
					continue;
				if(indexes[i]<N)
					break;
			}
			if(end)
				break;
		}
	}

	void print() {
		printf("%.9f",ans);
	}
};

int main(int argc, char** argv) {
	//std::ios_base::sync_with_stdio(false);
	//std::cin.tie(nullptr);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		Solver thisTestCase;
		thisTestCase.read();
		thisTestCase.solve();
		cout << "Case #" << t << ": ";
		thisTestCase.print();
		cout << endl;
	}
	return 0;
}
