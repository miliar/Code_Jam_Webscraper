#include <bits/stdc++.h>
using namespace std;



int main()
{
	int T; scanf("%d", &T);
	
	for(int tc = 1; tc <= T; tc++)
	{
		int N, R, Y, Bl, RY /*O*/, YB/*G*/, RB/*V*/;
		scanf("%d %d %d %d %d %d %d", &N, &R, &RY, &Y, &YB, &Bl, &RB);
		int r = R - YB, y = Y - RB, b = Bl - RY;
		
		if(N == 1)
		{
			if(R)
				printf("Case #%d: R\n", tc);
			if(RY)
				printf("Case #%d: O\n", tc);
			if(Y)
				printf("Case #%d: Y\n", tc);
			if(YB)
				printf("Case #%d: G\n", tc);
			if(Bl)
				printf("Case #%d: B\n", tc);
			if(RB)
				printf("Case #%d: V\n", tc);
			continue;
				
		}
		
		if(R == YB && Y == 0 && RB == 0 && Bl == 0 && RY == 0)
		{
			string sol = "";
			for(int i = 0; i < R; i++)
				sol += "RG";
			printf("Case #%d: %s\n", tc, sol.c_str());
			continue;
		}
		
		if(R == 0 && YB == 0 && Y == RB && Bl == 0 && RY == 0)
		{
			string sol = "";
			for(int i = 0; i < Y; i++)
				sol += "YV";
			printf("Case #%d: %s\n", tc, sol.c_str());
			continue;
		}
		
		if(R == 0 && YB == 0 && Y == 0 && RB == 0 && Bl == RY)
		{
			string sol = "";
			for(int i = 0; i < Bl; i++)
				sol += "BO";
			printf("Case #%d: %s\n", tc, sol.c_str());
			continue;
		}
		
		
		if((r == 0 && YB != 0) || (y == 0 && RB != 0) || (b == 0 && RY != 0))
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		
		pair<int, char> TEMP[3] = {make_pair(r, 'R'), make_pair(y, 'Y'), make_pair(b, 'B')};
		sort(TEMP, TEMP + 3);
		int A = TEMP[2].first, B = TEMP[1].first, C = TEMP[0].first;
		
		
		if(A < 0 || B < 0 || C < 0 || A > B + C)
		{
			printf("Case #%d: IMPOSSIBLE\n", tc);
			continue;
		}
		
		string sol0 = "";
		int i = 0;
		while(A + B > C)
		{
			if(i % 2 == 0)
			{
				sol0 += 'A';
				A--;
			}
			else
			{
				sol0 += 'B';
				B--;
			}
			
			i++;
			i %= 2; 
		}
		if(C != 0)
		{
			if(i % 2 == 0)
			{
				sol0 += 'A';
				A--;
			}
			else
			{
				sol0 += 'B';
				B--;
			}
			i++;
			i %= 2;
		}
		
		for(i = 0; i < C; i++)
		{
			sol0 += "C";
			if(A > 0)
			{
				sol0 += "A";
				A--;
			}
			else if(B > 0)
			{
				sol0 += "B";
				B--;
			}
		}
		
		for(int i = 0; i < (int)sol0.size(); i++)
		{
			if(sol0[i] == 'A')
				sol0[i] = TEMP[2].second;
			else if(sol0[i] == 'B')
				sol0[i] = TEMP[1].second;
			else if(sol0[i] == 'C')
				sol0[i] = TEMP[0].second;
		}
		
		bool Rok = false;
		bool Yok = false;
		bool Bok = false;
		
		string sol = "";
		for(int i = 0; i < sol0.size(); i++)
		{
			if(sol0[i] == 'R')
			{
				sol += "R";
				if(Rok) continue;
				Rok = true;
				if(YB == 0) continue;
				
				for(int k = 0; k < YB; k++)
					sol += "GR";
				
			}
			
			if(sol0[i] == 'Y')
			{
				sol += "Y";
				if(Yok) continue;
				Yok = true;
				if(RB == 0) continue;
				
				for(int k = 0; k < RB; k++)
					sol += "VY";
				
			}
			
			if(sol0[i] == 'B')
			{
				sol += "B";
				if(Bok) continue;
				Bok = true;
				if(RY == 0) continue;
				
				for(int k = 0; k < RY; k++)
					sol += "OB";
			}
		}
		
		printf("Case #%d: %s\n", tc, sol.c_str());
		
	}
	return 0;
}
