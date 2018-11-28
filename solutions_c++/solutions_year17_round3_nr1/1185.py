#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

double pi = 3.141592653;
double R[1000];
double H[1000];

struct aa {
	double R, H;
	double RH;
	
};

bool cmp(aa l, aa r) { return l.RH > r.RH; }
bool cmp2(aa l, aa r) { return l.R < r.R;  }
aa RH[1000];
aa RR[1000];
int main()
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("aaa.in");
	ofs.open("out");

	int T;
	ifs >> T;

	for (int i = 1; i <= T; i++)
	{
		int n, k;
		ifs >> n >> k;
		for (int j = 0; j < n; j++)
			ifs >> R[j] >> H[j];
		
		for (int j = 0; j < n; j++)
		{
			RH[j].R = R[j];
			RH[j].H = H[j];
			RH[j].RH = R[j] * H[j];
		}
		sort(RH, RH + n, cmp2);

		double ans = 0;
		for (int j = n - 1; j >= k - 1; j--)
		{
			double temp = RH[j].R * RH[j].R;
			for (int l = 0; l < j; l++)
			{
				RR[l] = RH[l];
			}
			sort(RR, RR + j, cmp);
			for (int l = 0; l < k - 1 ; l++)
				{
					temp += 2.0 * RR[l].RH;
				}

			temp += 2.0 * RH[j].RH;

			ans = max(temp, ans);
		}
		cout << i << endl;

		ofs << setprecision(8);
		ofs << fixed;
		ofs << "Case #" << i << ": " << ans  *  pi << endl;
	}
	system("pause");
	return 0;
}
