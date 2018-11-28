#include <bits/stdc++.h>

#define PAUSE system("pause")
#define LL long long int
#define ULL unsigned long long int
#define LD long double
#define PB push_back
#define PF push_front
#define MP make_pair
#define FORi(i, a, b) for(int i = a; i < b ; ++i)
#define FORd(i, a, b) for(int i = a; i > b ; --i)

using namespace std;

ULL last_tidy(ULL n){
	ULL rank = 10;
	while(n > rank/10){
		int d1 = n/rank%10;
		int d2 = n/(rank/10)%10;
		if (d1 > d2){
			n -= n%rank;
			n--;
		}
		rank *= 10;
//		cout << n << endl;
	}
	return n;
}

int main(int argc, char **argv)
{
	ifstream fin("/home/roman/CodeliteProjects/Competitive/GCJ17_Quals/in.txt");
	ofstream fout("/home/roman/CodeliteProjects/Competitive/GCJ17_Quals/out.txt");
	
	int t;
	fin >> t;
	FORi(testcase, 0, t){
		ULL n;
		fin >> n;
		fout << "Case #" << testcase+1 << ": " << last_tidy(n) << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
