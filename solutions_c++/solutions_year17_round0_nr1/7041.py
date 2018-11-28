#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;



int main() {
    
    //std::ifstream in("A-small-attempt0.in");
    /*std::ifstream in("A-large.in");
    std::streambuf *cinbuf = std::cin.rdbuf();
    std::cin.rdbuf(in.rdbuf());

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf();
    std::cout.rdbuf(out.rdbuf());
	*/
    int T;
    cin >> T;
    for1(tc, T) {
        cout << "Case #" << tc << ": ";
        string s;
        cin >> s;
        int k;
        cin>>k;
        int n = s.size();
        int count = 0,flag=1;
        int arr[1001]={0};
        forn(i,n)
        	arr[i]= s[i] == '-';
        forn(i,n-k+1)
        {
        	if(arr[i])
        	{
        		forn(j,k)
				{
					arr[i+j] = arr[i+j]^1;
				}
				++count;
        	}
        	else
				continue;
        }
		fore(i,n-k+1,n)
		{
			if(arr[i] == 1)
			{
				cout<<"IMPOSSIBLE"<<endl;
				flag=0;
				break;
			}
		}
		if(flag)
			cout<<count<<endl;
    }

	//std::cin.rdbuf(cinbuf);
    //std::cout.rdbuf(coutbuf);
    
    return 0;
}
