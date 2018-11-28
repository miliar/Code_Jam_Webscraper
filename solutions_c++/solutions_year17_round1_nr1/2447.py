#include <iostream>

using namespace std;

int T;
int R, C;
char table[30][30];

bool rowHasChar(int i)
{
	int j;
	for(j=0; j<C; j++)
	{
		if(table[i][j]!='?')
			break;
	}
	if(j == C)
		return false;
	else
		return true;
}

int findRow(int rs)
{
	int i;
	for(i=rs; i<R; i++)
	{
		if(rowHasChar(i)==true)
			break;
	}
	return i;
}

bool colHasChar(int j, int rs, int rn)
{
	int i;
	for(i=rs; i<=rn; i++)
	{
		if(table[i][j]!='?')
			break;
	}
	if(i > rn)
		return false;
	else
		return true;
}

int findCol(int cs, int rs, int rn)
{
	int j;
	for(j=cs; j < C; j++)
	{
		if(colHasChar(j, rs, rn)==true)
			break;
	}
	return j;
}

void fillTable(int rs, int rn, int cs, int cn, char cc)
{
	for(int i=rs; i<=rn; i++)
	{
		for(int j=cs; j<=cn; j++)
		{
			table[i][j] = cc;
		}
	}
}

void printTable()
{
	for(int i=0; i<R; i++)
	{
		for(int j=0; j<C; j++)
		{
			cout<< table[i][j];
		}
		cout<< endl;
	}
}

int main()
{
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		cin >> R >> C;
		for(int i=0; i<R; i++)
		{
			for(int j=0; j<C; j++)
			{
				cin >> table[i][j];
			}
		}
		int rstart = 0;
		int rnext;
		int cstart;
		int cnext;
		while(1)
		{
			rnext = findRow(rstart);
			if(rnext >= R)
				break;
			// cout<< rnext << endl;
			cstart = 0;
			while(1)
			{
				cnext = findCol(cstart, rstart, rnext);
				if(cnext >= C)
					break;
				// cout<< cnext << endl;
				// printTable();
				fillTable(rstart, rnext, cstart, cnext, table[rnext][cnext]);
				// printTable();
				cstart = cnext + 1;
			}
			rstart = rnext + 1;
		}
		for(int i=0; i < R; i++)
		{
			int j;
			for(j=0; j<C && table[i][j]!='?'; j++);
			if(j>0 && j<C)
			{
				// cout<< "here " << j << endl;
				char aa = table[i][j-1];
				for(int k = j; k < C; k++)
					table[i][k] = aa;
				// printTable();
			}
		}
		for(int j=0; j < C; j++)
		{
			int i;
			for(i=0; i<R && table[i][j]!='?'; i++);
			if(i>0 && i<R)
			{
				// cout<< "final" << i << endl;
				char aa = table[i-1][j];
				for(int k = i; k < R; k++)
					table[k][j] = aa;
				// printTable();
			}

		}
		cout<< "Case #" << t+1 << ":" << endl;
		printTable();
	}
	return 0;
}