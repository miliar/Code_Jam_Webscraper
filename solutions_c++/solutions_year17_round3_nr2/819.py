#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;
typedef long long int lli;
typedef pair<int, int> pii;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	
	int T, Ac, Aj, pl;
	cin >> T;
	for(int aa=1;aa<=T;++aa)
	{
		cin >> Ac >> Aj;
		int C[4], J[4];
		for(int i=0;i<Ac;++i)
			cin >> C[i*2] >> C[i*2+1];
		if(Ac > 1 && C[0] > C[2])
		{
			pl = C[0];
			C[0] = C[2];
			C[2] = pl;
			pl = C[1];
			C[1] = C[3];
			C[3] = pl;

			if(C[2] <= C[1])
			{
				C[1] = C[3];
				Ac=1;
			}
		}
		for(int i=0;i<Aj;++i)
			cin >> J[i*2] >> J[i*2+1];
		if(Aj > 1 && J[0] > J[2])
		{
			pl = J[0];
			J[0] = J[2];
			J[2] = pl;
			pl = J[1];
			J[1] = J[3];
			J[3] = pl;

			if(J[2] <= J[1])
			{
				J[1] = J[3];
				Aj=1;
			}
		}
		int ans = 0;
		if((Ac <2 && Aj < 2))
			ans = 2;
		else {
			if(Ac == 2)
			{
				if(C[0]-C[3]+1440 >= 720 || C[2]-C[1] >=720)
					ans = 2;
				else
					ans = 4;
			}
			else{
				if(J[0]-J[3]+1440 >= 720 || J[2]-J[1] >=720)
					ans = 2;
				else
					ans = 4;
			}
		}
		cout << "Case #" << aa << ": " << ans  << endl;
	}
	
	return 0;
}
