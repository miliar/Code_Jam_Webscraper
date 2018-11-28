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

pair<LL, LL> solve(LL n, LL k){
	map<LL, LL, greater<LL> > q1, q2;
	q1[n] = 1;
	LL l,r,cnt;
	while(k > 0){
		n = q1.begin()->first;
		cnt = q1.begin()->second;
		
		k -= cnt;
		q1.erase(q1.begin());
		
		l = (n+1)/2 - 1;
		r = n - (n+1)/2;
		
		q2[l] += cnt;
		q2[r] += cnt;
		
		if (q1.empty()){
			q1 = q2;
			q2.clear();
		}
	}
	return {r, l};
}

int main(int argc, char **argv)
{
	ifstream fin("/home/roman/CodeliteProjects/Competitive/GCJ17_Quals/in.txt");
	ofstream fout("/home/roman/CodeliteProjects/Competitive/GCJ17_Quals/out.txt");
	
	int t;
	fin >> t;
	FORi(testcase, 0, t){
		LL n, k;
		fin >> n >> k;
//		cout << "Test " << testcase+1 << endl;
		pair<LL, LL> res = solve(n, k);
		fout << "Case #" << testcase+1 << ": " << res.first << ' ' << res.second << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
