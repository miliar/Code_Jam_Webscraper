

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

	typedef struct
	{
		ld k;
		ld s;
	}horse;

struct distance_comparator
{
	bool operator() (const horse &lhs, const horse &rhs)
	{
		if (lhs.k <= rhs.k)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
};
int main() {
    //freopen("x.in", "r", stdin);
	int ans;
	//freopen("C-small-practice.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	multiset <horse, distance_comparator> s_h;
	multiset <horse, distance_comparator>:: iterator itr;
	multiset <horse, distance_comparator>:: iterator first_itr;
	multiset <horse, distance_comparator>:: iterator sec_itr;
	ll k[1000+1];
	ll s[1000+1];
	F1(tt,tn) {
		ld D, N;
		cin >> D >> N;
		F1(i, N)
		{
			horse temp;
			cin >> k[i];
			cin >> s[i];
			temp.k = k[i];
			temp.s = s[i];
			s_h.insert(temp);
		}

		ld wait_time = 0.0f;
		while (s_h.size() != 1)
		{
			itr = s_h.begin();
			first_itr = itr;
			horse first = *itr;

			sec_itr = ++itr;
			horse second = *(sec_itr);
				if (first.s > second.s)
				{
					ld t = ((ld)second.k-first.k)/(first.s-second.s);
					if (t <= (D-second.k)/second.s) /* Take care of eps */
					{
						/* Merge these two horses into one */
						s_h.erase(first_itr);
						s_h.erase(sec_itr);
						horse temp = {first.k+((first.s)*t) , second.s};
						s_h.insert(temp);
						wait_time += t;
					}
					else
					{
						break;
					}
				}
				else if (first.s == second.s)
				{
					if (first.k == second.k)
					{
						s_h.erase(itr);
					}
					else
					{
						break;
					}	
				}
				else
				{
					break;
				}
		}
		
		itr = s_h.begin();
		horse first = *itr;
		ld t = ((ld)D - first.k)/first.s;
		ld s = D/(t+wait_time);
		s_h.clear();
		//cout << "Case #" << tt << ": " << s << endl;
		printf("Case #%d: %0.6lf\n", (tt), (double)s);
	}
}
