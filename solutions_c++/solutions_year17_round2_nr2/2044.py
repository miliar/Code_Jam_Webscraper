#include <iostream>
#include <sstream>
#include <string>

using namespace std;

stringstream out;

enum type
{
	o,
	b,
	g,
	r,
	v,
	y,
};


void func()
{
	int n;
	cin >> n;
	int t[6];
	cin >> t[r] >> t[o] >> t[y] >> t[g] >> t[b] >> t[v];

	string output[3];

	while (t[o] > 0 && t[b] > 0)
	{
		output[0] += "OB";
		t[o]--;
		t[b]--;
	}

	if (t[b] > 0 && !output[0].empty())
	{
		output[0] = "B" + output[0];
		t[b]--;
	}

	while (t[g] > 0 && t[r] > 0)
	{
		output[1] += "GR";
		t[g]--;
		t[r]--;
	}

	if (t[r] > 0 && !output[1].empty())
	{
		output[1] = "R" + output[1];
		t[r]--;
	}

	while (t[v] > 0 && t[y] > 0)
	{
		output[2] += "VY";
		t[v]--;
		t[y]--;
	}

	if (t[y] > 0 && !output[2].empty())
	{
		output[2] = "Y" + output[2];
		t[y]--;
	}

	if (output[0][0] == 'O' && !output[1].empty() && !output[2].empty())
	{
		out << "IMPOSSIBLE\n";
		return;
	}
	if (output[1][0] == 'G' && !output[0].empty() && !output[2].empty())
	{
		out << "IMPOSSIBLE\n";
		return;
	}
	if (output[2][0] == 'V' && !output[0].empty() && !output[1].empty())
	{
		out << "IMPOSSIBLE\n";
		return;
	}

	string add_output;

	while (t[r] > 0 || t[b] > 0 || t[y] > 0)
	{
		if (t[r] >= t[b] && t[r] >= t[y])
		{
			add_output += "R";
			t[r]--;
			t[r] = abs(t[r]);
			t[b] = abs(t[b]);
			t[y] = abs(t[y]);
			t[r] = -t[r];

			if (t[b] == 0 && t[y] == 0)
				break;

		}

		else if (t[b] >= t[r] && t[b] >= t[y])
		{
			add_output += "B";
			t[b]--;


			t[r] = abs(t[r]);
			t[b] = abs(t[b]);
			t[y] = abs(t[y]);
			t[b] = -t[b];

			if (t[r] == 0 && t[y] == 0)
				break;

		}

		else
		{
			add_output += "Y";
			t[y]--;


			t[r] = abs(t[r]);
			t[b] = abs(t[b]);
			t[y] = abs(t[y]);
			t[y] = -t[y];

			if (t[b] == 0 && t[r] == 0)
				break;
		}
	}

	bool added = false;

	if (add_output.length() > 2 && add_output[add_output.length() - 1] != add_output[add_output.length() - 3] && add_output[add_output.length() - 1] == add_output[0])
		swap(add_output[add_output.length() - 1], add_output[add_output.length() - 2]);

	if (!add_output.empty())
	{
		char first = add_output[0];
		char last = add_output[add_output.length() - 1];

		for (int i = 0; i < 3; i++)
		{
			if (output[(i + 1) % 3][0] != last && output[i][output[i].length()] != first)
			{ 
				output[i] += add_output;
				added = true;
				break;
			}
		}
	}

	

	if (!add_output.empty() && !added)
	{
		char first = add_output[0];
		char last = add_output[add_output.length() - 1];

		for (int i = 0; i < 3; i++)
		{
			if (output[(i + 1) % 3][0] != last && output[i][output[i].length()] != first)
			{
				output[i] += add_output;
				added = true;
				break;
			}
		}
	}

	string outputfull = output[0] + output[1] + output[2];

	for (int i = 0; i < outputfull.length(); i++)
	{
		if (outputfull[i] == outputfull[(i + 1) % (outputfull.length())])
		{
			out << "IMPOSSIBLE\n";
			return;
		}
	}

	if (outputfull.length() < n || *outputfull.begin() == outputfull.back())
		out << "IMPOSSIBLE\n";
	else
		out << outputfull << endl;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ": ";
		func();
	}
	cout << out.str();
	return 0;
}