
#include <bits/stdc++.h>

using namespace std;


int main()
{
	int T;
	int N,P,temp;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		cout <<"Case #"<<t <<": ";
		cin >> N >> P;
		vector<int> required;
		for(int i = 0; i < N;i++)
		{
			cin >> temp;
			required.push_back(temp);
		}

		deque< deque<int> > v(N, deque<int>(P, 0) );
		for(int i = 0; i <  N; i++){
			for(int j = 0; j < P; j++)
				cin >> v[i][j];
			sort(v[i].begin(), v[i].end());
		}

		int res  = 0;
		int a ,b, x, y;
		int flag, flag2,flag3;

		for(int i = 0 ; i < P; i++)
		{	
			//cerr << "P: " << P << " i:" << i << endl;
			flag = 1;
			flag2 = 1;
			flag3 = 1;
			a = ceil(1.0 * v[0][i]/(1.1*required[0]));
			b = 1.0 * v[0][i]/(0.9*required[0]);

			//cerr << a << b << endl;
			if (a > b) continue;
			for(int j = 1; j < N; j++)
			{
				if (v[j].size() < 1 )
				{
					flag2 = 0;
					flag = 0;
					break;
				}
				int k = v[j].front();
				x = ceil(1.0 * k/(1.1*required[j]));
				y = 1.0 * k/(0.9*required[j]);
				//	cerr << a << " "<<b << " "<<x << " " << y << endl;
				if (x > y)
				{
					v[j].pop_front();
					flag = 0;
					break;
				}
				if (!((x >= a && x <= b ) || (y >= a && y <= b)))
				{
					//v[j].pop_front();
					flag = 0;
					flag3 = 0;
				}

			}

			if (flag)
			{
				for(int j = 1; j < N; j++)
					v[j].pop_front();
			}

			res += flag;
			if (flag == 0 && flag2 != 0)
				i--;
			if (flag3 == 0)
				i++;

		}

		cout << res << endl;

		
	}
	return 0;
}