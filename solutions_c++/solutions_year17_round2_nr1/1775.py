#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)


bool submit = true;

// ---------------------------------------------------
// ---------------------------------------------------



int main()
 {
	if (submit)
	{
		// freopen("A-small-attempt0.in", "r", stdin);
		// freopen("A-small-attempt0.out", "w", stdout);
		
		freopen("A-large.in", "r", stdin);
		freopen("A-large.out", "w", stdout);

		int tt, tn; // loop var and total test cases
		cin >> tn;

		F1(tt,tn)
		{
			int D, N;
			cin >> D;
			cin >> N;

			float maxTime = 0.0f;
			vector<pair<int, int>> h;
			F0(i, N)
			{
				int d, s;
				cin >> d; cin >> s;
				maxTime = max(maxTime, (D-d)/static_cast<float>(s));
			}
			printf("Case #%d: ", tt);
			printf("%f\n", D/maxTime);

		}
	}

	return 0;
}
