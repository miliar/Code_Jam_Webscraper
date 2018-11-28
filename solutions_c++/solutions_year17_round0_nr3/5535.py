#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

int main()
{
	int a[1002] = {0};
	int tt;
	std::ifstream inp("input_c.txt");
	std::ofstream outp("output_c.txt");

	inp >> tt;
	for (int t = 1; t <= tt; ++t)
	{
		outp << "Case #" << t << ": ";
		int n, k;
		inp >> n >> k;
		memset(a, 0, sizeof(a));
		a[0] = 1;
		a[n+1] = 1;
		for (int kk = 0; kk < k; kk++)
		{
			int minlr = -1, maxlr = -1;
			int index = 0;
			for (int i = 1; i <= n; i++)
				if (a[i] == 0)
				{
					int left = 0;
					int li = i - 1;
					while(a[li] == 0)
					{
						left++;
						li--;
					}
					int right = 0;
					int ri = i + 1;
					while(a[ri]== 0)
					{
						right++;
						ri++;
					}
					int tminlr = std::min(left,right);
					int tmaxlr = std::max(left,right);
					if (minlr < tminlr || (minlr == tminlr && maxlr < tmaxlr))
					{
						minlr = tminlr;
						maxlr = tmaxlr;
						index = i;
					}
				}
			a[index] = 1;
			if (kk == k-1)
			{
				outp << maxlr << " " << minlr;
			}
		}
		if (t != tt)
			outp << std::endl;
	}

	outp.close();
	inp.close();
	return 0;
}