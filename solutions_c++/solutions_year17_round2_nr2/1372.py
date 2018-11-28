#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>
#include <iomanip>
#include <sstream>

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());
	string line;
	string imp = "IMPOSSIBLE";
	int T = 0, N, R, O, Y, G, B, V;
	vector<string> result;

	if (file.is_open())
	{
		file >> T;
		result.resize(T);

		for (int i = 0; i < T; ++i)
		{
			file >> N >> R >> O >> Y >> G >> B >> V;

			vector<string> Bstring;
			vector<string> Ystring;
			vector<string> Rstring;

			if (R+Y+G+V == 0)
			{
				if (B == O)
				{
					stringstream ss;
					for (size_t j = 0; j < B; j++)
					{
						ss << 'B' << 'O';
					}
					result[i] = ss.str();
				}
				else
				{
					result[i] = imp;
				}
				continue;
			}
			else if (O > 0 && B < O + 1)
			{
				result[i] = imp;
				continue;
			}

			if (R + O + G + B == 0)
			{
				if (Y == V)
				{
					stringstream ss;
					for (size_t j = 0; j < Y; j++)
					{
						ss << 'Y' << 'V';
					}
					result[i] = ss.str();
				}
				else
				{
					result[i] = imp;
				}
				continue;
			}
			else if (V>0 && Y < V + 1)
			{
				result[i] = imp;
				continue;
			}
			
			if (O + Y + V + B == 0)
			{
				if (R == G)
				{
					stringstream ss;
					for (size_t j = 0; j < R; j++)
					{
						ss << 'R' << 'G';
					}
					result[i] = ss.str();
				}
				else
				{
					result[i] = imp;
				}
				continue;
			}
			else if (G>0 && R < G + 1)
			{
				result[i] = imp;
				continue;
			}
			
			B -= O + 1;
			Y -= V + 1;
			R -= G + 1;
			for (int j = 0; j < B; j++)
			{
				Bstring.push_back("B");
			}
			if (B >= 0)
			{
				stringstream ssB;
				for (int j = 0; j < O; j++)
				{
					ssB << 'B' << 'O';
				}
				ssB << 'B';
				Bstring.push_back(ssB.str());
			}

			for (int j = 0; j < Y; j++)
			{
				Ystring.push_back("Y");
			}
			if (Y >= 0)
			{
				stringstream ssY;
				for (int j = 0; j < V; j++)
				{
					ssY << 'Y' << 'V';
				}
				ssY << 'Y';
				Ystring.push_back(ssY.str());
			}

			for (int j = 0; j < R; j++)
			{
				Rstring.push_back("R");
			}
			if (R >= 0)
			{
				stringstream ssR;
				for (int j = 0; j < G; j++)
				{
					ssR << 'R' << 'G';
				}
				ssR << 'R';
				Rstring.push_back(ssR.str());
			}

			B++;
			R++;
			Y++;

			int maxS, midS, minS;
			vector<string> maxString, midString, minString;

			if (B >= R)
			{
				if (B >= Y)
				{
					maxS = B;
					maxString = Bstring;

					if (Y >= R)
					{
						midS = Y;
						midString = Ystring;

						minS = R;
						minString = Rstring;
					}
					else
					{
						midS = R;
						midString = Rstring;

						minS = Y;
						minString = Ystring;
					}
				}
				else
				{
					maxS = Y;
					maxString = Ystring;

					midS = B;
					midString = Bstring;

					minS = R;
					minString = Rstring;
				}
			}
			else
			{
				if (B >= Y)
				{
					maxS = R;
					maxString = Rstring;

					midS = B;
					midString = Bstring;

					minS = Y;
					minString = Ystring;
				}
				else
				{
					minS = B;
					minString = Bstring;

					if (Y >= R)
					{
						maxS = Y;
						maxString = Ystring;

						midS = R;
						midString = Rstring;
					}
					else
					{
						maxS = R;
						maxString = Rstring;

						midS = Y;
						midString = Ystring;
					}
				}
			}
			
			if (maxS > midS + minS)
			{
				result[i] = imp;
				continue;
			}

			vector<string> K, L, M;
			
			for (int j = 0; j < midS; j++)
			{
				K.push_back(maxString[j].append(midString[j]));
			}

			for (int j = 0; j < maxS-midS; j++)
			{
				L.push_back(maxString[j + midS].append(minString[j]));
			}

			for (int j = maxS - midS; j < minS; j++)
			{
				M.push_back(minString[j]);
			}

			stringstream ssResult;
			for (int j = 0; j < maxS; j++)
			{
				if (K.size() >= j+1)
				{
					ssResult << K[j];
				}
				if (M.size() >= j + 1)
				{
					ssResult << M[j];
				}
				if (L.size() >= j + 1)
				{
					ssResult << L[j];
				}
			}
			result[i] = ssResult.str();
		}
	}

	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");
	for (int i = 0; i < T; ++i)
	{
		outputfile << "Case #" << i + 1 << ": " << fixed << std::setprecision(6) << result[i];
		if (i != (T - 1))
			outputfile << endl;
	}
	outputfile.close();

	return 0;
}