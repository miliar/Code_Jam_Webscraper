#include<fstream>

using namespace std;

#define N 1001

char stalls[N];
int colors[6];

int get_max(int c1, int c2)
{
	if (colors[c1] <= 0 && colors[c2] <= 0) return -1;
	if (colors[c1] < colors[c2]) return c2;
	
	return c1;
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;

	for (int test_case = 0; test_case < T; test_case++)
	{
		int n, R, O, Y, G, B, V;
		int current = 0, left = 0, first_color;
		bool possible = true;
		
		/*in >> n >> R >> O >> Y >> G >> B >> V;*/
		in >> n;
		for (int i = 0; i < 6; i++) 
		{
			in >> colors[i];
			left += colors[i];
		}

		//left = R + O + Y + G + B + V;
		for (first_color = 0; first_color < 6 && colors[first_color]<=0; first_color += 2);
			
		possible = first_color < 6;
		if (possible)
		{
			colors[first_color]--;
			left--;
			stalls[0] = first_color;
		}

		while (left > 0 && possible && current < n)
		{
			if (stalls[current] == 1)
			{
				if (colors[4] <= 0)
				{
					possible = false;
					break;
				}
				else
				{
					current++;
					stalls[current] = 4;
					colors[4]--;
					left--;
					continue;
				}
			}

			if (stalls[current] == 3)
			{
				if (colors[0] <= 0)
				{
					possible = false;
					break;
				}
				else
				{
					current++;
					stalls[current] = 0;
					colors[0]--;
					left--;
					continue;
				}
			}

			if (stalls[current] == 5)
			{
				if (colors[2] <= 0)
				{
					possible = false;
					break;
				}
				else
				{
					current++;
					stalls[current] = 2;
					colors[2]--;
					left--;
					continue;
				}
			}

			if (stalls[current] == 0)
			{
				if (colors[3] > 0)
				{
					colors[3]--;
					current++;
					stalls[current] = 3;
					left--;
					continue;
				}
				else
				{
					int choice = get_max(2, 4);
					if (choice == -1)
					{
						possible = false;
						break;
					}
					current++;
					stalls[current] = choice;
					colors[choice]--;
					left--;
					continue;
				}
			}

			if (stalls[current] == 2)
			{
				if (colors[5] > 0)
				{
					colors[5]--;
					current++;
					stalls[current] = 5;
					left--;
					continue;
				}
				else
				{
					int choice = get_max(0, 4);
					if (choice == -1)
					{
						possible = false;
						break;
					}
					current++;
					stalls[current] = choice;
					colors[choice]--;
					left--;
					continue;
				}
			}

			if (stalls[current] == 4)
			{
				if (colors[1] > 0)
				{
					colors[1]--;
					current++;
					stalls[current] = 1;
					left--;
					continue;
				}
				else
				{
					int choice = get_max(0, 2);
					if (choice == -1)
					{
						possible = false;
						break;
					}
					current++;
					stalls[current] = choice;
					colors[choice]--;
					left--;
					continue;
				}
			}
		}

		if (possible)
		{
			if (stalls[0] == stalls[n - 1])
			{
				possible = false;
				int col = stalls[0], c1, c2, i;
				if (col == 0)
				{
					c1 = 2;
					c2 = 4;
				}
				if (col == 2)
				{
					c1 == 0;
					c2 = 4;
				}
				if (col == 4)
				{
					c1 = 0;
					c2 = 2;
				}
				
				for (i = 1; i < n - 2; i++)
				{
					if (stalls[i] == c1 && stalls[i - 1] == c2 && stalls[i + 1] == c2)
					{
						possible = true;
						stalls[0] = c1;
						stalls[i] = col;
						break;
					}
					if (stalls[i] == c2 && stalls[i - 1] == c1 && stalls[i + 1] == c1)
					{
						possible = true;
						stalls[0] = c2;
						stalls[i] = col;
						break;
					}
				}
			}
		}

		out << "Case #" << test_case + 1<< ": ";
		if (!possible)
		{
			out << "IMPOSSIBLE" << endl;
		}
		else
		{
			for (int i = 0; i < n; i++)
			{
				if (stalls[i] == 0) stalls[i] = 'R';
				if (stalls[i] == 1) stalls[i] = 'O';
				if (stalls[i] == 2) stalls[i] = 'Y';
				if (stalls[i] == 3) stalls[i] = 'G';
				if (stalls[i] == 4) stalls[i] = 'B';
				if (stalls[i] == 5) stalls[i] = 'V';
			}
			for (int i = 0; i < n; i++)
			{
				out << stalls[i];
			}
			out << endl;
		}
	}
}