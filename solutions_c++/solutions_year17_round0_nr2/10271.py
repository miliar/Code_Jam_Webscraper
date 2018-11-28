/*       Rohan Balot     
    NSIT, New Delhi, India  */
#include <bits/stdc++.h>
using namespace std;
                                         
#define ALL(t) (t).begin(), (t).end()
#define ALLR(t) (t).rbegin(), (t).rend()
#define MP make_pair
             
const int N = int( 1e6 ) + 1;
const int MOD = int( 1e9 ) + 7;

bool ok(long long num) 
{
	vector<int> d;
	while (num) {
		d.emplace_back(num % 10);
		num /= 10;
	}
	for (int i = d.size() - 1; i - 1 >= 0; i--) {
		if(d[i] > d[i - 1])
			return 0;
	}
	return 1;
}
void __answer()
{
	long long n, ans = 0LL;
	cin >> n;
	for(long long i = n; i >= 1; i--) {
		if(ok(i)) {
			cout << i << '\n';
			break;
		}
	}
}

int main()
{	
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	clock_t s = clock();
    #ifdef LOCAL
      freopen("sample_input.txt", "r", stdin);
	#endif
    #ifndef LOCAL
      freopen("B-small-attempt0.in", "r", stdin);
	  freopen("B-small.txt", "w", stdout);
	#endif
	size_t _t;
    cin >> _t;
    cin.ignore();
	for (register size_t _i = 1; _i <= _t; _i++){
        cout << "Case #" << _i << ": ";
		__answer();
	}
	cerr << "Time = " << (0.001 * (clock() - s)) << " s\n";
    return 0;
}