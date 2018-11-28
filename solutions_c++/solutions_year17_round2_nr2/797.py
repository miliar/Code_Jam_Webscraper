#include <bits/stdc++.h>

using namespace std;
typedef long long int ll;
#define BR __int("$3");

int n, r, o, y, g, b, v;
int rx, yx, bx;
int last;

bool putr()
{
	if (!rx) return false;
	while (g-- > 0) cout << "RG";
	cout << "R";
	rx--;
	last=1;
	return true;
}

bool puty()
{
	if (!yx) return false;
	while (v-- > 0) cout << "YV";
	cout << "Y";
	yx--;
	last=2;
	return true;
}

bool putb()
{
	if (!bx) return false;
	while (o-- > 0) cout << "BO";
	cout << "B";
	bx--;
	last=3;
	return true;
}

inline int max3(int a, int b, int c)
{
	return max(a, max(b, c));
}

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		cin >> n >> r >> o >> y >> g >> b >> v;
		if ((r==g) && (o+y+b+v==0))
		{
			cout << "Case #" << tt << ": ";
			while (r--) cout << "RG";
			cout << endl;
			continue;
		}
		if ((o==b) && (r+y+g+v==0))
		{
			cout << "Case #" << tt << ": ";
			while (b--) cout << "OB";
			cout << endl;
			continue;
		}
		if ((y==v) && (o+r+b+g==0))
		{
			cout << "Case #" << tt << ": ";
			while (y--) cout << "YV";
			cout << endl;
			continue;
		}
		rx=r-g;
		yx=y-v;
		bx=b-o;
		if ((rx < 0) || (yx < 0) || (bx < 0) || 
				((rx == 0) && (g > 0)) ||
				((yx == 0) && (v > 0)) ||
				((bx == 0) && (o > 0)) ||
				(rx > yx + bx) || (yx > bx + rx) || (bx > rx + yx))
		{
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
		}
		else
		{
			cout << "Case #" << tt << ": ";
			if (!putr()) puty();
			while (rx || yx || bx)
			{
				switch (last)
				{
					case 1:
						if (yx >= bx) puty();
						else putb();
						break;
					case 2:
						if (rx >= bx) putr();
						else putb();
						break;
					case 3:
						if (rx >= yx) putr();
						else puty();
						break;
				}
			}
			cout << endl;
		}
	}
	return 0;
}
