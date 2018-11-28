#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>

using namespace std;

int T, N;
int R, O, Y, G, B, V;
int src;

vector<char> result;

bool dfs(int cur, int type)
{
	if (cur == 0)
		return !(src & type);

	switch (type)
	{
	case 4:	// RED
		if (G)
		{
			if (G-- && dfs(cur - 1, 3))
			{
				result.push_back('G');
				return true;
			}
			else
				G++;
		}
		else
		{
			if (Y >= B)
			{
				if (Y-- && dfs(cur - 1, 2))
				{
					result.push_back('Y');
					return true;
				}
				else
					Y++;
			}
			else
			{
				if (B-- && dfs(cur - 1, 1))
				{
					result.push_back('B');
					return true;
				}
				else
					B++;
			}
		}
		break;
	case 6:	// ORAcurGE = RED + YELLOW
		if (B-- && dfs(cur - 1, 1))
		{
			result.push_back('B');
			return true;
		}
		else
			B++;
		break;
	case 2:	// YELLOW
		if(V)
		{
			if (V-- && dfs(cur - 1, 5))
			{
				result.push_back('V');
				return true;
			}
			else
				V++;
		}
		else
		{
			if (R >= B)
			{
				if (R-- && dfs(cur - 1, 4))
				{
					result.push_back('R');
					return true;
				}
				else
					R++;
			}
			else
			{
				if (B-- && dfs(cur - 1, 1))
				{
					result.push_back('B');
					return true;
				}
				else
					B++;
			}
		}
		
		break;
	case 3:	// GREEcur = YELLOW + BLUE
		if (R-- && dfs(cur - 1, 4))
		{
			result.push_back('R');
			return true;
		}
		else
			R++;
		break;
	case 1:	// BLUE
		if (O)
		{
			if (O-- && dfs(cur - 1, 6))
			{
				result.push_back('O');
				return true;
			}
			else
				O++;
		}
		else
		{
			if (R >= Y)
			{
				if (R-- && dfs(cur - 1, 4))
				{
					result.push_back('R');
					return true;
				}
				else
					R++;
			}
			else
			{
				if (Y-- && dfs(cur - 1, 2))
				{
					result.push_back('Y');
					return true;
				}
				else
					Y++;
			}
		}
		break;
	case 5:	// VIOLET = RED + BLUE
		if (Y-- && dfs(cur - 1, 2))
		{
			result.push_back('Y');
			return true;
		}
		else
			Y++;
		break;
	default:
		break;
	}

	return false;
}

int main()
{
	FILE *in = fopen("in.txt", "r");
	FILE *out = fopen("out.txt", "w+");

	fscanf(in, "%d", &T);
	for(int t = 1 ; t <= T ; t++)
	{
		printf("%d\n", t);
		result.clear();
		fscanf(in, "%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

		if (R)
			src = 4, R--;
		else if (O)
			src = 6, O--;
		else if (Y)
			src = 2, Y--;
		else if (G)
			src = 3, G--;
		else if (B)
			src = 1, B--;
		else if (V)
			src = 5, V--;
		else
			src = -1;

		fprintf(out, "Case #%d: ", t);
		if (dfs(N - 1, src))
		{
			switch (src)
			{
			case 1:
				result.push_back('B');
				break;
			case 2:
				result.push_back('Y');
				break;
			case 3:
				result.push_back('G');
				break;
			case 4:
				result.push_back('R');
				break;
			case 5:
				result.push_back('V');
				break;
			case 6:
				result.push_back('O');
				break;
			default:
				result.push_back(NULL);
				break;
			}
			int size = (int)result.size();
			for (int i = 0; i < size ; i++)
				fprintf(out, "%c", result[i]);
			fprintf(out, "\n");
		}
		else
			fprintf(out, "IMPOSSIBLE\n");
	}

	fclose(in);
	fclose(out);

	return 0;
}