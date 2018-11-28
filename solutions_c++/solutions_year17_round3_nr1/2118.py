#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std; 

typedef vector< pair<int, int> > vp;

double calc_area(vp& vv, int k);

double calc_area(vp& vv, int k)
{
	const double PI = M_PI;
	double ar;
	ar = PI * (vv[0].first) * (vv[0].first);

	for (int i = 0; i < k; i++)
	{
		ar += 2 * PI * vv[i].first * vv[i].second;
	}

	return ar;
}

int main() 
{
	int t;
	scanf("%d", &t); 
	for (int x = 1; x <= t; x++)
	{
		vp v;
		int n, k;
		scanf("%d %d", &n, &k);

		for (int i = 0; i < n; i++)
		{
			int r, h;
			scanf("%d %d", &r, &h);
			v.push_back(make_pair(r, h));
		}

		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());

		string bm(k, 1); 
    	bm.resize(n, 0);

    	double max = 0.0;

    	do
	    {
	    	vp vv;

	        for (int i = 0; i < n; i++) 
	        {
	            if (bm[i]) 
	         		vv.push_back(v[i]);
	        }

	        double ar = calc_area(vv, k);
	        if (ar >= max)
	        	max = ar;
	        
	    } while (prev_permutation(bm.begin(), bm.end()));

	    printf("Case #%d: %.9f\n", x, max);
	}

	return 0;
}

