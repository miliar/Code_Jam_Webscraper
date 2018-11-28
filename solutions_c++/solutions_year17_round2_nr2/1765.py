#include <iostream>
#include <algorithm>
#include <iomanip>
#include <string>

using namespace std;

#define PR(X,Y,Z) ((X > Y)||(X == Y && out.length() == 0)||(X == Y && out.front() != Z))

int main()
{
	int T;

	cin >> T;

	int N, R, O, Y, G, B, V;

	for (int t = 1; t <= T; t++)
	{
	
		cin >> N >> R >> O >> Y >> G >> B >> V;

		string out = "";

		char last = '0';

		while (N > 0)
		{
			bool p = false;

			if (((last == '0' || last == 'B') && PR(Y,R,'R')) ||
				((last == '0' || last == 'R') && PR(Y,B,'B')))
			{
				while (Y > 0 && V > 0)
				{
					p = true;
					out.append("YV");
					Y--;
					V--;
					N = N - 2;
					last = 'V';
				}

				if (V > 0)
				{
					out = "IMPOSSIBLE";
					goto done;
				}

				if (Y > 0)
				{
					p = true;
					out.append("Y");
					Y--;
					N--;
					last = 'Y';
				}
			}

			if (((last == '0' || last == 'Y') && PR(B,R,'R')) ||
				((last == '0' || last == 'R') && PR(B,Y,'Y')))
			{
				while (B > 0 && O > 0)
				{
					p = true;
					out.append("BO");
					B--;
					O--;
					N = N - 2;
					last = 'O';
				}

				if (O > 0)
				{
					out = "IMPOSSIBLE";
					goto done;
				}

				if (B > 0)
				{
					p = true;
					out.append("B");
					B--;
					N--;
					last = 'B';
				}
			}

			if (((last == '0' || last == 'Y') && PR(R,B,'B')) ||
				((last == '0' || last == 'B') && PR(R,Y,'Y')))
			{
				while (R > 0 && G > 0)
				{
					p = true;
					out.append("RG");
					R--;
					G--;
					N = N - 2;
					last = 'G';
				}

				if (G > 0)
				{
					out = "IMPOSSIBLE";
					goto done;
				}

				if (R > 0)
				{
					p = true;
					out.append("R");
					R--;
					N--;
					last = 'R';
				}
			}

			if (!p)
			{
				out = "IMPOSSIBLE";
				goto done;
			}
		}

		if (out.front() == out.back())
		{
			out = "IMPOSSIBLE";
		}

	done:

		cout << "Case #" << t << ": " << out << endl;
	}

	return 0;
}