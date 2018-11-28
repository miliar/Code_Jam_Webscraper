#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <set>

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define FORC(it,cont) for(__typeof(cont.begin()) it=(cont).begin(); it!=(cont).end();++(it))
#define VI vector<int>
#define VS vector<string>
#define pb push_back

using namespace std;

long long toint(string s) {
	long long sol = 0;
	FOR(i,0,s.size())
		sol = sol*10 + s[i] - '0';
	return sol;	
}

string tostr(long long x) {
	string s;
	while(x){
		s += (char)(x%10 + '0');
		x/=10;
	}
	reverse(s.begin(),s.end());
	return s;
}

bool istidy(long long x) {
	string s = tostr(x);
	FOR(i,1,s.size())
		if(s[i]<s[i-1])
			return false;
	return true;	
}

long long largesttidy(long long n) {
	for(long long i = n; i >=0; --i )
		if(istidy(i)) return i;
	return 0;
}

long long solve(long long N) {
	long long res;
	string s = tostr(N);
	bool other = false;
	string s2;
	FOR(i,0,s.size()) {
		bool smaller = false;
		bool larger =  false;
		int j = i+1;
		while( j < s.size() && smaller == false) {
			if(s[i] > s[j]) smaller = true;
			else if( s[i] < s[j] ) larger = true;
			++j;
		}
		
		if(!larger && smaller) {
			s2 = s;
			s2[i] -= 1;
			FOR(j,i+1,s.size()) s2[j] = '9';
			other = true;
			break;
		}
	}
	if (other) res = toint(s2);
	else res = N;
	return res;
}


int main()
	{
	int T,N;
	ifstream fcin("B-large.in",ios::in);
	//ifstream fcin("in.txt",ios::in);
	FILE* fout;
	fout = fopen("out.txt","w");
	fcin >> T;
	FOR(tc,0,T)
		{
		long long res = 0;
		long long N; fcin >> N;
		//cout << N << endl;
		
		//FOR(i,0,1000)
		//	if(solve(i) != largesttidy(i))
		//		cout << i << " " << solve(i) << " " << largesttidy(i) << endl;
		res = solve(N);
		
		fprintf(fout,"Case #%d: %lld\n",tc+1,res);
		}
	fcin.close();
	return 0;
	}

