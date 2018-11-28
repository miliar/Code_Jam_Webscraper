// GOD knows how I feel

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int maxx = 110;

int a[maxx], tt, n, t[4] ,p;



int main()
{
//	ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out"); 
	in >> tt;
	for(int u = 1; u <= tt; u++)
	{
		out << "Case #" << u << ": ";
		in >> n >> p; t[0] = t[1] = t[2] = t[3] = 0;
		for(int i = 0; i < n; i++)
			in >> a[i], t[a[i] % p]++;
		if(p == 2)
		{
			out << t[0] + ((t[1] + 1) / 2) << endl;
//			continue;
		}
		else if (p == 3)
		{
			int x = t[0] + min(t[1], t[2]);
			if (t[1] <= t[2])
				t[2] -= t[1], x += (t[2] / 3) + (t[2] % 3 != 0);
//			cout << t[0] + min(t[1], t[2]);
			else
				t[1] -= t[2], x += (t[1] / 3) + (t[1] % 3 != 0);
			out << x << endl;
		}
		else
		{
			int x = t[0];
			x += (t[2] / 2);
			t[2] %= 2;
			x += min(t[1], t[3]);
			int g = min(t[1], t[3]);
			t[1] -= g;
			t[3] -= g;
			if (t[1] < t[3])
				t[1] = t[3];
			if (t[2] == 0)
			{
				x += (t[1] / 4) + (t[1] % 4 != 0);
				out << x << endl;
			}
			else
			{
				x ++;
				if (t[1] <= 2) out << x << endl;
				else
				{
					t[1] -= 2;
					x += (t[1] / 4) + (t[1] % 4 != 0);
					out << x << endl;
				}
			}
		}
	}
	return 0;
}
