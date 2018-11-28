#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class pos{
	public:
	int distance;
	int startIdx;
	int endIdx;
	pos() {
	}
	pos(int d,int s,int e) {
		distance = d;
		startIdx = s;
		endIdx = e;
	}
	struct Compare
	{
		bool operator()(const pos &p1 , const pos &p2 ) const
		{
			return p1.distance < p2.distance;
		}
	};

};

static void display(pos &p){ 
				cout << "elements:" << p.endIdx+1 <<" " << endl;
			}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.precision(10);
	cout << fixed;

	int T;
	cin >> T;
	for(int to=1;to<=(int)T;++to){
		cout << "Case #"<< to <<": ";
		string s;
		int N,K;
		cin >> N;
		cin >> K;
#ifdef LOCAL_DEFINE
		cout <<" stalls:" << N << " K people:" << K << "  \n";
#endif
		vector<pos> v;
		v.push_back(pos(N,0,N-1));

		int ndL,ndR;
		pos p1,p2;
		for(int j = 0;j<K; j++){
			pos maxv = *max_element(v.begin(),v.end(),pos::Compare());
			v.erase(max_element(v.begin(),v.end(),pos::Compare()));
			int nIdx = maxv.distance%2==1?maxv.distance/2+1+maxv.startIdx-1:maxv.distance/2+maxv.startIdx-1;
			ndL = nIdx - maxv.startIdx;
			ndR = maxv.endIdx - nIdx;
			p1 = pos(ndL,maxv.startIdx,nIdx-1);
			p2 = pos(ndR,nIdx+1,maxv.endIdx);
#ifdef LOCAL_DEFINE
			cout << "maxv.distance:" << maxv.distance << " nIdx:" << nIdx << "\n";
			cout << "ndL:" << ndL << " startIdx:"<< maxv.startIdx << " endIdx:"<< nIdx << " \n";
			cout << "ndR:" << ndR << " startIdx:"<< nIdx+1<< " endIdx:"<< maxv.endIdx << " \n";
#endif
			v.push_back(p1);
			v.push_back(p2);
		}
		int ls,rs;
		for(pos p:v){
			if(p.endIdx == (p1.startIdx-1)){
				ls = p1.endIdx - p.startIdx;
			}
		}
		rs = p2.endIdx - p2.startIdx;
		int max = ndL>ndR?ndL:ndR;
		int min = ndL>ndR?ndR:ndL;
		cout <<  max << " " << min << "\n";
	}
#ifdef LOCAL_DEFINE
	cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
	return 0;
}

