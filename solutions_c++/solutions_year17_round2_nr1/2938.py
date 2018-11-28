


#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	std::ios_base::sync_with_stdio(false);
/*
	freopen("inputL.in","r", stdin);
	freopen("outputL.txt","w", stdout);
	*/
	int t;
	std::cin >> t;

	int z=1;
	while(z<=t)
	{
		long long d,n;
		std::cin >> d >> n;

		double max = 0.0;

		for(int i=0; i<n; i++)
		{
			double pos,speed,tmp;
			std::cin >> pos >> speed;

			tmp = (d-pos)/speed;
			if(tmp > max)
				max = tmp;
		}

		double ans = d/max;
		printf("Case #%d: %.6f\n",z,ans);
		z++;
	}
}
