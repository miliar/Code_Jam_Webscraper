#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>

#define _CRT_SECURE_NO_DEPRECATE // suppress some compilation warning messages (for VC++ users)
#define iOS std::ios_base::sync_with_stdio(false)
#define sqr(a) (((a) * (a)))
#define REP(i,a) for(int i=0;i!=int(a);i++)


typedef long long ll;
typedef unsigned long long ull;
typedef std::vector<int> vi;
typedef std::pair<int, int> ii;
typedef std::vector<ii> vii;
typedef std::set<int> si;
typedef std::map<std::string, int> msi;


#define INF 2000000000 // 2 billion
// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers

ull doTidy()
{
	ull input;
	std::cin >> input;
	int log = 1;
	ull log10=10;
	while (log10 <= input) { log++; log10 *= 10; }
	ull d = 100;
	for (int i = 1; i < log; i++, d*=10)
	{
		if (((input%d - input%(d/10))/(d/10)) > ((input%(d/10) - input % (d / 100)) / (d / 100))) {
			input -= std::min((input%(d/10))+1, (((input%d - input % (d / 10)) / (d / 10)) - ((input % (d / 10) - input % (d / 100)) / (d / 100)))*(d/10)+1);
		}		
	}



	return input;
}


int main()
{
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; i++)
	{
		std::cout << "Case #" << i << ": " << doTidy()<<"\n";
	}

	return 0;

}