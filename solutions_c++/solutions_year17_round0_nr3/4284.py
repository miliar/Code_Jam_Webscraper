#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;


ll f1(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - (k - numRepeats / 2)) / numRepeats;
}

ll f2(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - k) / numRepeats;
}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	string s;
	ll k,n;

	bool ar[1000];
	int left[1000];
	int right[1000];

	int ans;
	int len;

	bool stupid = 1;

	for (int t = 0; t < T; ++t)
	{
		input >> n>>k;

		if (!stupid)
		{
			for (int i = 0; i < n; ++i)
			{
				ar[i] = 0;
			}

			int bestMin = 0;
			int bestMax = 0;

			for (int i = 0; i < k; ++i)
			{
				bestMin = -1;
				bestMax = -1;
				int bestIndex = -1;

				for (int i = 0; i < n; ++i)
				{
					if (ar[i] == 0)
					{
						int left = 0;
						int right = 0;

						int j = i - 1;
						while (j >= 0 && ar[j] == 0)
						{
							--j;
							++left;
						}
						j = i + 1;
						while (j < n && ar[j] == 0)
						{
							++j;
							++right;
						}

						if (min(left, right)>bestMin || (min(left, right) == bestMin && max(left, right) > bestMax))
						{
							bestIndex = i;
							bestMin = min(left, right);
							bestMax = max(left, right);
						}
					}
				}

				//_ASSERT(bestIndex != -1);
				ar[bestIndex] = 1;
			}


			output << "Case #" << t + 1 << ": " << bestMax << ' ' << bestMin << endl;
		}
		else
		{
			ll alt1 = f1(n, k), alt2 = f2(n, k);
			output << "Case #" << t + 1 << ": " << alt1 << ' ' << alt2 << endl;
			
		}

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
